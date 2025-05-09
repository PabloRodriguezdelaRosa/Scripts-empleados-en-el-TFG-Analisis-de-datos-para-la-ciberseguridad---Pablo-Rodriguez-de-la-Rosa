import random

# Leer todas las líneas del archivo
with open("final_dataset.csv", "r") as fichero:
    lineas = fichero.readlines()

# Separar la cabecera de los datos
cabecera = lineas[0]
datos = lineas[1:]

# Filtrar los registros y limitar la cantidad de cada clase
ddos_samples = [linea for linea in datos if "ddos" in linea][:500000]
benign_samples = [linea for linea in datos if "Benign" in linea][:500000]

# Mezclar los registros seleccionados
mezclados = ddos_samples + benign_samples
random.shuffle(mezclados)  # Mezclar aleatoriamente

# Escribir los datos mezclados en el nuevo archivo
with open("final_dataset_1000k.csv", "w") as fichero_salida:
    fichero_salida.write(cabecera)  # Escribir la cabecera
    fichero_salida.writelines(mezclados)  # Escribir los datos mezclados

# Ahora generamos el dataset de test
ddos_test_samples = [linea for linea in datos if "ddos" in linea][500000:550000]
benign_test_samples = [linea for linea in datos if "Benign" in linea][500000:550000]

# Mezclar los datos de test
mezclados_test = ddos_test_samples + benign_test_samples
random.shuffle(mezclados_test)

# Escribir el dataset de test
with open("test_simulation_dataset_100k.csv", "w") as fichero_salida_2:
    fichero_salida_2.write(cabecera)
    fichero_salida_2.writelines(mezclados_test)

# Mensaje de confirmación
print(f"Archivo 'final_dataset_1000k.csv' generado con 500000 líneas de 'ddos' y 500000 líneas de 'benign'.")
print(f"Archivo 'test_simulation_dataset_100k.csv' generado con 50000 líneas de 'ddos' y 50000 líneas de 'benign'.")
