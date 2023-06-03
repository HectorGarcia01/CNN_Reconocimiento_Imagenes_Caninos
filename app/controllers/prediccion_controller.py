from flask import request, redirect, render_template, session, url_for, current_app, flash
from random import sample
from werkzeug.utils import secure_filename   
import os
import numpy as np
import json
from scipy.special import softmax
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from models.prediccion import Prediccion                              #Cargamos la clase Prediccion
from main import db  


#Definimos una función para generar un string aleatorio
def stringAleatorio():
    #Definimos el string
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"

    #Definimos la longitud
    longitud         = 20

    #Convertimos el string a mayusculas
    secuencia        = string_aleatorio.upper()

    #Generamos un resultado aleatorio
    resultado_aleatorio  = sample(secuencia, longitud)

    #Unimos el string aleatorio
    string_aleatorio     = "".join(resultado_aleatorio)

    #Retornamos el string aleatorio
    return string_aleatorio

#Definimos una función para la predicción del modelo
def realizar_prediccion(ruta_imagen):
    longitud, altura = 256, 256 #para caninos

    # Definimos la ruta del modelo
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_modelo = os.path.join(ruta_base, '../../src/Modelo_entrenado/modelo_caninos.h5')

    #Cargamos el modelo
    modelo_cargado = load_model(ruta_modelo)

    #Definimos la ruta del archivo JSON
    ruta_json = os.path.join(ruta_base, '../../src/Modelo_entrenado/clases_Canino.json')

    #Cargamos el archivo JSON con el mapeo de clases
    with open(ruta_json, 'r') as f:
        mapeo_clases = json.load(f)
        print(mapeo_clases) #Imprimimos el contenido del json para observar las clases

    #Ajustamos el tamaño de la imagen
    imagen = load_img(ruta_imagen, target_size=(altura, longitud))

    #Convertimos la imagen a un array de NumPy
    imagen_array = img_to_array(imagen)
    imagen_array = np.expand_dims(imagen_array, axis=0)

    #Hacemos la predicción con el modelo
    prediccion = modelo_cargado.predict(imagen_array)

    #Obtenemos las probabilidades de pertenencia a cada clase aplicando la función softmax
    probabilidades = softmax(prediccion)[0]

    #Obtenemos los nombres de las clases
    nombre_clases = list(mapeo_clases.keys())

    #Definimos una lista vacía para almacenar las predicciones
    lista_prediccion = []

    #Imprimimos los porcentajes de pertenencia a cada clase
    for i, name in enumerate(nombre_clases):
        #Realizamos el cálculo del porcentaje para cada clase
        porcentaje = round(probabilidades[i] * 100, 2)

        #Agregamos el porcentaje a la lista de predicciones
        lista_prediccion.append(porcentaje)

    #Retornamos la lista
    return lista_prediccion

#Definimos una función para la predicción
def guardar_prediccion():
    try:
        #Obtenemos la imagen enviada desde el formulario
        imagen = request.files['imagen']

        #Nombre original de la imagen
        nombre_original = secure_filename(imagen.filename)

        #Capturando las extensiones de la imagen
        extension_imagen = os.path.splitext(nombre_original)[1]

        #Establecemos un nuevo nombre para la imagen
        nuevo_nombre_imagen = stringAleatorio() + extension_imagen

        #Guardamos la imagen en la carpeta definida
        ruta_img = os.path.join(current_app.root_path, 'static', 'img', nuevo_nombre_imagen)

        #Guardamos la imagen en la ruta dada
        imagen.save(ruta_img)

        #Llamamos la función para realizar la predicción
        lista_prediccion = realizar_prediccion(ruta_img)

        #Obtenemos el porcentaje de predicción para cada variable
        porcentaje_coyote = lista_prediccion[0]
        porcentaje_lobo = lista_prediccion[1]
        porcentaje_perro = lista_prediccion[2]
        porcentaje_zorro = lista_prediccion[3]

        #Obtenemos el id del usuario de la sesión
        id_usuario_fk = session['id_usuario']

        #Creamos una nueva instancia de Prediccion con los datos proporcionados
        prediccion = Prediccion(porcentaje_perro, porcentaje_lobo, porcentaje_zorro, porcentaje_coyote, ruta_img, id_usuario_fk)

        #Guardamos la nueva predicción
        db.session.add(prediccion)

        #Finalizamos la conexión para que guarde el nuevo usuario a la bd
        db.session.commit()

        #Renderizamos el template y cada predicción de clase
        return render_template('prediccion.html', 
                            porcentaje_coyote=porcentaje_coyote, 
                            porcentaje_lobo=porcentaje_lobo, 
                            porcentaje_perro=porcentaje_perro, 
                            porcentaje_zorro=porcentaje_zorro,
                            ruta_img=url_for('static', filename=f'img/{nuevo_nombre_imagen}'))
    
    except Exception as e:
        #Redireccionamos a la ruta de prediccion de felinos
        return redirect('/prediccion/felinos')

#Definimos una función para todas las predicciones del usuario
def obtener_predicciones():
    try:
        #Verificamos si en sesiones hay un id del usuario
        if not 'id_usuario' in session:
            #Mostramos una alerta con SweetAlert2
            flash('Primero debe de autenticarse.', 'error')

            #Redireccionamos a la ruta del login
            return redirect('/login')
        
        #Obtenemos el id del usuario de la sesión
        id_usuario_fk = session['id_usuario']

        #Buscamos todas las predicciones del usuario
        usuario_predicciones = Prediccion.query.filter_by(id_usuario_fk=id_usuario_fk).all()

        #Verificamos si se encontró un usuario
        if usuario_predicciones:
            #Obtenemos el nombre de archivo de la imagen en cada predicción
            for prediccion in usuario_predicciones:
                nombre_imagen = os.path.basename(prediccion.imagen_prediccion)
                prediccion.imagen_prediccion = url_for('static', filename=f'img/{nombre_imagen}')
            
            #Renderizamos el template perfil.html y pasamos los datos del usuario
            return render_template('ver_predicciones.html', predicciones=usuario_predicciones)

    except Exception as e:
        #Redireccionamos a la ruta del login
        return redirect('/prediccion/felinos')
