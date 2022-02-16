#Ejercicio 1
jupiterDistance = 778547200
earthDistance = 149597870
#Distancia entre Jupiter y la tierra
distanceBetweenPLanet = jupiterDistance - earthDistance
print (f"""La distancia entre ellos es : {distanceBetweenPLanet} Km""")
distanceBetweenPLanetMiles = distanceBetweenPLanet * 0.621371
print (f"""La distancia entre ellos es : {distanceBetweenPLanetMiles} Millas""")
#ejercicio 2
firstPlanet = input('Introduzce la distancia del sol para el primer planeta(kilometros)')
secondPlanet = input('Introduzce la distancia del sol para el segundo planeta(kilometros)')
firstPlanet = int(firstPlanet)
secondPlanet = int(secondPlanet)
distanceBetweenPlanets = secondPlanet - firstPlanet
print(distanceBetweenPlanets)
distanceBetweenPlanetsToMiles = distanceBetweenPlanets * 0.621
print(abs(distanceBetweenPlanetsToMiles))