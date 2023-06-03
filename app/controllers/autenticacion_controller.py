from flask import request, render_template, redirect, session, flash
from models.usuario import Usuario                              #Cargamos la clase Usuario

#Definimos la función para validar las credenciales del usuario
def validar_credenciales():
    try:
        #Obtenemos los datos del formulario
        correo = request.form['correo']
        password = request.form['password']

        #Buscamos el usuario en la bd por su correo
        usuario = Usuario.query.filter_by(correo=correo).first()

        #Validamos si las contraseñas coinciden
        if usuario and usuario.verificar_contraseña(password):
            #Creamos una sesión con el id del usuario
            session['id_usuario'] = usuario.id

            #Redireccionamos a la ruta para la predicción
            return redirect('/prediccion/felinos')
        else:
            #Mostramos una alerta con SweetAlert2
            flash('Las credenciales ingresadas no son válidas.', 'error')

            #Redireccionamos al mismo login
            return redirect('/login')
    except Exception as e:
        #Redireccionamos al mismo login
        return redirect('/login')

#Definimos una función para verificar la sesión del usuario para la predicción
def verificar_sesion_pred():
    #Verificamos si en sesiones hay un id del usuario
    if not 'id_usuario' in session:
        #Mostramos una alerta con SweetAlert2
        flash('Primero debe de autenticarse.', 'error')

        #Redireccionamos a la ruta login
        return redirect('/login')
    
    #Renderizamos el template predicción
    return render_template('prediccion.html')

#Definimos una función para cerrar la sesión del usuario
def logout_usuario():
    #Borramos la sesión
    session.pop('id_usuario', None)

    #Redireccionamos a la ruta para cerrar sesión
    return redirect('/login')