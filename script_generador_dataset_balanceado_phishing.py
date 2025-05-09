import random

# Leer todas las líneas del archivo
with open("dataset_full.csv", "r") as fichero:
    lineas = fichero.readlines()

# Separar la cabecera de los datos
cabecera = lineas[0]
datos = lineas[1:]

cabecera = lineas[0]
datos = lineas[1:]

# Modificar la última columna para marcar phishing y legitimate
datos_modificados = []
for linea in datos:
    valores = linea.strip().split(",")
    if valores[-1] == "1":
        valores[-1] = "phishing"
    else:
        valores[-1] = "legitimate"
    datos_modificados.append(",".join(valores) + "\n")

# Filtrar los registros y limitar la cantidad de cada clase
legitimate_samples = [linea for linea in datos_modificados if "legitimate" in linea][:25000]
phishing_samples = [linea for linea in datos_modificados if "phishing" in linea][:25000]

# Mezclar los registros seleccionados
mezclados = legitimate_samples + phishing_samples
random.shuffle(mezclados)  # Mezclar aleatoriamente

# Escribir los datos mezclados en el nuevo archivo
with open("dataset_full_50k.csv", "w") as fichero_salida:
    fichero_salida.write(cabecera)  # Escribir la cabecera
    fichero_salida.writelines(mezclados)  # Escribir los datos mezclados

# Ahora generamos el dataset de test
legitimate_samples_test = [linea for linea in datos_modificados if "legitimate" in linea][25000:]
phishing_samples_test = [linea for linea in datos_modificados if "phishing" in linea][25000:]

# Mezclar los datos de test
mezclados_test = legitimate_samples_test + phishing_samples_test
random.shuffle(mezclados_test)

# Escribir el dataset de test
with open("test_simulation_dataset.csv", "w") as fichero_salida_2:
    fichero_salida_2.write(cabecera)
    fichero_salida_2.writelines(mezclados_test)

print("Proceso finalizado")
