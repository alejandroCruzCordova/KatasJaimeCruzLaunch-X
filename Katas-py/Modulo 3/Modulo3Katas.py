#Obtener la velocidad del asteroide
print("Advertencias sobre asteroides")
velocityAsteroid = input("Velocidad del asteroide (km/s): ")
sizeAsteroid= input("Tamaño del asteroide (metros):")
if int(velocityAsteroid) > 25:
    print("Advertencia asteroide acercandose rapidamente!!")

if int(velocityAsteroid) >= 20:
    print("Buscar un asteroide en el cielo, Será visible")
else:
    print("El asteroide no tiene la velocidad suficiente para hacerse visible")

if int(sizeAsteroid) < 25:
    print("Se quemará en la atmosfera")
elif (int(sizeAsteroid) > 25 and int(sizeAsteroid) < 1000):
    print("El impacto tendrá graves daños a la tierra!!")
