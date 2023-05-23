import os

# path = './Caninos/train/zorro' # Ruta de la carpeta donde posee las imagenes
# prefix = 'zorro_train_' # Prefijo para el nuevo nombre de la imagen

path = './Caninos/val/zorro' # Ruta de la carpeta donde posee las imagenes
prefix = 'zorro_val_' # Prefijo para el nuevo nombre de la imagen

count = 1 # Contador para incrementar el número en el nombre de la imagen

for filename in os.listdir(path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'): # Verifica si la extensión del archivo es .jpg, .jpeg o .png
        new_filename = prefix + str(count) + os.path.splitext(filename)[1] # Agrega la extensión original del archivo al nuevo nombre
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        count += 1

print("Listo xd")