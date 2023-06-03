from bcrypt import hashpw, gensalt
from main import db #Cargamos la instacia db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)        #Definimos el atributo id como llave primaria
    nombre = db.Column(db.String(30))                   #Definimos el atributo para el nombre del usuario
    apellido = db.Column(db.String(30))                 #Definimos el atributo para el apellido del usuario
    direccion = db.Column(db.String(50))                #Definimos el atributo para la dirección del usuario
    correo = db.Column(db.String(30), unique=True)      #Definimos el atributo para el correo del usuario y la establecemos como unica 
    password = db.Column(db.String(100))                #Definimos el atributo para la contraseña del usuario

    #Definimos el constructor para pasar los datos a la bd
    def __init__(self, nombre, apellido, direccion, correo, password):
        self.nombre = nombre                                                            #Asignamos el valor proporcionado al atributo nombre
        self.apellido = apellido                                                        #Asignamos el valor proporcionado al atributo nombre
        self.direccion = direccion                                                      #Asignamos el valor proporcionado al atributo nombre
        self.correo = correo                                                            #Asignamos el valor proporcionado al atributo nombre
        self.password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')     #Asignamos el valor proporcionado al atributo password pero encriptada

    #Definimos una función para verificar la contraseña del login con la contraseña de la bd
    def verificar_contraseña(self, password):
        return hashpw(password.encode('utf-8'), self.password.encode('utf-8')) == self.password.encode('utf-8')  #Verifica si la contraseña proporcionada coincide con la contraseña almacenada en forma de hash