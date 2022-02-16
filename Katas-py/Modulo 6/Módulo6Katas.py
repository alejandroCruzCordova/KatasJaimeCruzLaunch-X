#Ejercicio 1
planets = ['Mercurio', 'Venus', 'Tierra', 'Martes', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
print(planets)

planets.append('Pluton')
print(planets)

#Ejercicio 2
planets = ['Mercurio', 'Venus', 'Tierra', 'Martes', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
searchPlanet = input('Introduce el planeta (Escribe la primera letra del planeta en mayuscula): ')
planetPosition = planets.index(searchPlanet)
closestPlanets = planets[0:planetPosition]
print("Planetas más cercanos")
print(closestPlanets)
farthestPlanets = planets[planetPosition+1:]
print(farthestPlanets)