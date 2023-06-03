from dotenv import load_dotenv
import os

load_dotenv()

#Obtenemos nuestras constantes de configuración del .env
host = os.environ['NOMBRE_HOST']
usuario = os.environ['USUARIO_BD']
password = os.environ['PASSWORD_BD']
nombre_bd = os.environ['NOMBRE_BD']
clave_secreta_flask = os.environ['CLAVE_FLASK']

#Definimos la URL de conexión a la base de datos
URI_CONEXION_BD = f'mysql://{usuario}:{password}@{host}/{nombre_bd}'