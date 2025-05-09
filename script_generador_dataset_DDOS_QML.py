import random

# Leer todas las líneas del archivo
def cargar_datos(ruta):
    with open(ruta, "r") as fichero:
        lineas = fichero.readlines()
    return lineas[0], lineas[1:]  # Retornar cabecera y datos

# Cargar datos desde el dataset
cabecera, datos = cargar_datos("final_dataset.csv")

# Filtrar registros por clase
registros_ddos = [linea for linea in datos if "ddos" in linea]
registros_benign = [linea for linea in datos if "Benign" in linea]

# Seleccionar 50 registros aleatorios de cada clase
muestra_ddos = random.sample(registros_ddos, 100) if len(registros_ddos) >= 100 else registros_ddos
muestra_benign = random.sample(registros_benign, 100) if len(registros_benign) >= 100 else registros_benign

# Unir y mezclar las muestras
muestra_final = muestra_ddos + muestra_benign
random.shuffle(muestra_final)

# Guardar el nuevo dataset
with open("balanced_dataset_100_2.csv", "w") as fichero_salida:
    fichero_salida.write(cabecera)
    fichero_salida.writelines(muestra_final)

print("Archivo 'balanced_dataset_100.csv' generado con 50 registros 'ddos' y 50 registros 'benign'.")
