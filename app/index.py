from main import crear_app, db               #Cargamos la instancia db y la función crear_app

#Obtenemos la instancia app de la función
app = crear_app()

#Para que cree todas las tablas que hemos definido en los modelos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    #Inicializamos el servidor web
    app.run(debug=True)