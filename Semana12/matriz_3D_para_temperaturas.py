#Crear una matriz en 3D para almacenar datos de temperatura
# Definimos las ciudades, días de la semana y semanas

ciudades = ['Ciudad A - Cuenca', 'Ciudad B - Quito', 'Ciudad C - Loja']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Creamos una matriz 3D con temperaturas específicas
# Dimensiones: [ciudades, días, semanas]
matriz_temp = [
    [ # Ciudad A - Cuenca
        [20, 22, 21, 19], # Lunes
        [21, 13, 20, 22], # Martes
        [19, 20, 21, 20], # Miércoles
        [22, 21, 23, 24], # Jueves
        [24, 25, 26, 25], # Viernes
        [26, 27, 28, 27], # Sábado
        [23, 22, 24, 25]  # Domingo
    ],
    [ # Ciudad B - Quito
        [25, 26, 27, 24], # Lunes
        [26, 27, 28, 25], # Martes
        [24, 25, 26, 27], # Miércoles
        [27, 25, 26, 27], # Jueves
        [29, 18, 17, 19], # Viernes
        [15, 17, 20, 18], # Sábado
        [20, 22, 21, 15]  # Domingo
    ],
    [ # Ciudad C - Loja
        [15, 16, 17, 15], # Lunes
        [17, 16, 18, 20], # Martes
        [17, 15, 22, 23], # Miércoles
        [20, 21, 22, 24], # Jueves
        [18, 17, 19, 20], # Viernes
        [19, 15, 25, 27], # Sábado
        [22, 25, 27, 29]  # Domingo
    ]
]
# Calcular el promedio de temperaturas para cada ciudad por semanas

for ciudad in range(len(matriz_temp)): # ciudades
    suma_mes = []
    for semana in range(semanas):
        suma = 0
        for dia in range(len(dias)):
            suma += matriz_temp[ciudad][dia][semana]
        suma_prom = suma / len(dias)
        suma_mes.append(suma_prom)
# Mostrar el promedio de las temperaturas para cada ciudad y semanas

        print(f'El promedio de la semana {semana + 1} es: {suma_prom:.2f} para la ciudad de {ciudades[ciudad].split(" - ")[1]}.')
    suma_mes_prom = sum(suma_mes) / semanas
    print(f'El promedio de la temperatura en {ciudades[ciudad].split(" - ")[1]} en este mes fue de {suma_mes_prom:.2f} °C')

#Se definieron temperaturas para cada ciudad y semana. Cada ciudad tiene un conjunto de temperaturas para cada uno de
#7 dias de la semana durante 4 semanas. El calculo de promedios se mantiene utilizando bucles anidados para recorrer la
#matriz y calcular el promedio de temperaturas por ciudad y semanas.