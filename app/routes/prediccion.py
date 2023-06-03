from flask import Blueprint 
from controllers.autenticacion_controller import verificar_sesion_pred           #Cargamos la función verificar_sesion_pred del controlador
from controllers.prediccion_controller import guardar_prediccion                 #Cargamos la función guardar_prediccion del controlador
from controllers.prediccion_controller import obtener_predicciones               #Cargamos la función obtener_predicciones del controlador

#Creamos la sección para las rutas de predicción
rutas_prediccion = Blueprint('prediccion', __name__)

#Configuramos la ruta para la predicción
@rutas_prediccion.route('/prediccion/felinos')
def prediccion():
    #Retornamos la función verificar_sesion_pred
    return verificar_sesion_pred()

#Configuramos la ruta para guardar los datos del usuario
@rutas_prediccion.route('/prediccion/nueva_prediccion', methods=['POST'])
def nueva_prediccion():
    #Retornamos la función para guardar la nueva prediccion a la bd
    return guardar_prediccion()

#Configuramos la ruta para ver todas las predicciones del usuario
@rutas_prediccion.route('/prediccion/ver')
def datos_predicciones():
    #Retornamos la función obtener_usuario
    return obtener_predicciones()