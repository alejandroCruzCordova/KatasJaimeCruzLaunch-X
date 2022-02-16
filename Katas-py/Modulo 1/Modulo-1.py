#modulo-1.py
sum = 1 + 2
print(sum)
#Hola desde consola

print('Hola desde consola')

#Variables
sum = 1 + 2 #3
product = sum * 2
print (product) 

#Tipos de datos

planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

#Conocer el tipo de dato

distancia_a_alfa_centauri = 4.367
print(type(distancia_a_alfa_centauri))

#Operadores
left_side = 10
right_side = 5
operacion = left_side / right_side # 2
print(operacion)

#Fechas
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())
#print("Today's date is: "+ date.today()) Error porque date no es cadena
print("Today's date is: " + str(date.today()))


