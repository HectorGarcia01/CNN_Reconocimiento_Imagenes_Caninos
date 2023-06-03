from flask import request, render_template, redirect, session, flash
from models.usuario import Usuario                              #Cargamos la clase Usuario
from main import db                                             #Cargamos la instancia db

#Definimmos la función para guardar los datos en la bd
def guardar_usuario():
    try:
        #Obtenemos los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        correo = request.form['correo']
        password = request.form['password']

        #Instanciamos la clase Usuario para crear uno nuevo objeto
        nuevo_usuario = Usuario(nombre, apellido, direccion, correo, password)

        #Guardamos el nuevo usuario
        db.session.add(nuevo_usuario)

        #Finalizamos la conexión para que guarde el nuevo usuario a la bd
        db.session.commit()

        #Mostramos una alerta con SweetAlert2
        flash('Usuario creado con éxito.')

        #Redireccionamos a la ruta para el registro de usuario
        return redirect('/registro/usuario')
    except Exception as e:
        #Redireccionamos a la ruta para el registro de usuario
        return redirect('/registro/usuario')

#Definimos una función para obtener los datos del usuario
def obtener_usuario():
    try:
        #Verificamos si en sesiones hay un id del usuario
        if not 'id_usuario' in session:
            #Mostramos una alerta con SweetAlert2
            flash('Primero debe de autenticarse.', 'error')

            #Redireccionamos a la ruta del login
            return redirect('/login')
        
        #Obtenemos el id del usuario de la sesión
        id_usuario = session['id_usuario']

        #Buscamos el usuario en la bd por su id
        usuario = Usuario.query.get(id_usuario)

        #Verificamos si se encontró un usuario
        if usuario:
                #Renderizamos el template perfil.html y pasamos los datos del usuario
                return render_template('perfil.html', usuario=usuario)

    except Exception as e:
        #Redireccionamos a la ruta del login
        return redirect('/login')
