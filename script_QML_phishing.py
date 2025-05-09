import random

# Leer todas las líneas del archivo
def cargar_datos(ruta):
    with open(ruta, "r") as fichero:
        lineas = fichero.readlines()
    return lineas[0], lineas[1:]  # Retornar cabecera y datos

# Cargar datos desde el dataset
cabecera, datos = cargar_datos("dataset_full_50k.csv")

# Filtrar registros por clase
registros_phishing = [linea for linea in datos if "phishing" in linea]
registros_legitimate = [linea for linea in datos if "legitimate" in linea]

# Seleccionar 50 registros aleatorios de cada clase
muestra_phishing = random.sample(registros_phishing, 50) if len(registros_phishing) >= 50 else registros_phishing
muestra_legitimate = random.sample(registros_legitimate, 50) if len(registros_legitimate) >= 50 else registros_legitimate

# Unir y mezclar las muestras
muestra_final = muestra_phishing + muestra_legitimate
random.shuffle(muestra_final)

# Guardar el nuevo dataset
with open("balanced_dataset_100_phishing.csv", "w") as fichero_salida:
    fichero_salida.write(cabecera)
    fichero_salida.writelines(muestra_final)

print("Archivo 'balanced_dataset_100.csv' generado con 50 registros 'phishing' y 50 registros 'legitimate'.")
