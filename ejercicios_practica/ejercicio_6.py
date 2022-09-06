# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

from itertools import count



inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

positivos = 0
negativos = 0
lista_completa = []

for i in range(inicio , fin + 1 ):
    lista_completa.append(i)
    

for i in lista_completa:
    if i >= 0:
        positivos = positivos + 1
        
    
    if i < 0:
        negativos = negativos + 1
           

print("La cantidad de numeros negativos es: ", negativos)  
print("La cantidad de numeros positivos mas el cero es: ", positivos)    

# for ... in range(....)

    
       


# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
