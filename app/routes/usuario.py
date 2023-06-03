from flask import Blueprint, render_template, redirect
from controllers.usuario_controller import guardar_usuario                  #Cargamos la función guardar_usuario del controlador
from controllers.autenticacion_controller import validar_credenciales       #Cargamos la función validar_credenciales del controlador
from controllers.usuario_controller import obtener_usuario                  #Cargamos la función obtener_usuario del controlador
from controllers.autenticacion_controller import logout_usuario             #Cargamos la función logout_user del controlador

#Creamos la sección para las rutas de usuarios
rutas_usuario = Blueprint('usuario', __name__)

#Configuramos la ruta raíz para redirigir al login
@rutas_usuario.route('/')
def root():
    return redirect('/login')

#Configuramos la ruta para el login
@rutas_usuario.route('/login')
def login():
    #Renderizamos el template login
    return render_template('login.html')

#Configuramos la ruta para la validación de credenciales
@rutas_usuario.route('/login/validar_usuario', methods=['POST'])
def validar_usuario():
    #Retornamos la función para validar credenciales del login
    return validar_credenciales()

#Configuramos la ruta para el registro de usuarios
@rutas_usuario.route('/registro/usuario')
def registro():
    #Renderizamos el template registro
    return render_template('registro.html')

#Configuramos la ruta para guardar los datos del usuario
@rutas_usuario.route('/registro/nuevo_usuario', methods=['POST'])
def nuevo_usuario():
    #Retornamos la función para guardar el usuario en la db
    return guardar_usuario()

#Configuramos la ruta para ver el perfil del usuario
@rutas_usuario.route('/usuario/perfil')
def perfil_usuario():
    #Retornamos la función obtener_usuario
    return obtener_usuario()

#Configuramos la ruta para cerrar sesión
@rutas_usuario.route('/usuario/logout')
def cerrar_sesion():
    #Retornamos la función logout_usuario
    return logout_usuario()