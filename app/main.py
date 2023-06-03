from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import URI_CONEXION_BD, clave_secreta_flask  #Cargamos la constante que posee la url de conexión y la clave secreta de flask

#Creamos una instancia de Flask y definimos la ruta static
app = Flask(__name__)

#Agregamos la clave secreta para el uso de sesiones
app.secret_key = clave_secreta_flask

#Configuramos la bd
app.config['SQLALCHEMY_DATABASE_URI'] = URI_CONEXION_BD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Pasamos la instancia de app a SQLAlchemy
db = SQLAlchemy(app)

#Definimos una función para agregar las rutas a la instancia app
def crear_app():
    from routes.usuario import rutas_usuario            #Cargamos las rutas del usuario
    from routes.prediccion import rutas_prediccion      #Cargamos las rutas de las predicciones

    #Agregamos las rutas del usuario a la aplicación
    app.register_blueprint(rutas_usuario)

    #Agregamos las rutas de las predicciones
    app.register_blueprint(rutas_prediccion)

    #Retornamos la instancia app
    return app