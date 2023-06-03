from main import db #Cargamos la instacia db

class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)                                #Definimos el atributo id como llave primaria
    porcentaje_perro = db.Column(db.String(20))                                  #Definimos el atributo para la predicción de leon
    porcentaje_lobo = db.Column(db.String(20))                                  #Definimos el atributo para el predicción de gato
    porcentaje_zorro = db.Column(db.String(20))                                 #Definimos el atributo para la predicción de tigre
    porcentaje_coyote= db.Column(db.String(20))                                #Definimos el atributo para el predicción de pantera
    imagen_prediccion = db.Column(db.String(500))                               #Definimos el atributo para la imagen de la predicción
    id_usuario_fk = db.Column(db.Integer, db.ForeignKey('usuario.id'))          #Definimos el atributo para el id del usuario con llave foranea

    #Definimos el constructor para pasar los datos a la bd
    def __init__(self, porcentaje_perro, porcentaje_lobo, porcentaje_zorro, porcentaje_coyote, imagen_prediccion, id_usuario_fk):
        self.porcentaje_perro = porcentaje_perro                                                        #Asignamos el valor proporcionado al atributo porcentaje_leon
        self.porcentaje_lobo = porcentaje_lobo                                                        #Asignamos el valor proporcionado al atributo porcentaje_gato
        self.porcentaje_zorro = porcentaje_zorro                                                      #Asignamos el valor proporcionado al atributo porcentaje_tigre
        self.porcentaje_coyote = porcentaje_coyote                                                  #Asignamos el valor proporcionado al atributo porcentaje_pantera
        self.imagen_prediccion = imagen_prediccion                                                   #Asignamos el valor proporcionado al atributo imagen_prediccion
        self.id_usuario_fk = id_usuario_fk                                                       #Asignamos el valor proporcionado al atributo id_usuario_fk