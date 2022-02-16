planet = {
    'name': 'Mars',
    'moon': 2
}

print(f"The Planet: {planet ['name']} have {planet.get('moon')} moon's")

planet.update({
    'circunferencia' :{
        'polar': 6752,
        'equatorial': 6792
    }
})

print(f"The Planet: {planet ['name']} have {planet ['circunferencia']['polar']} polar circumference")

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

for moons in planet_moons.keys():
    print(f'{moons}: {planet_moons[moons]}')
planets = len(planet_moons.keys())

total_moons=0
for moons in planet_moons.keys():
    total_moons = total_moons + planet_moons[moons]
average_moons = total_moons / planets

print(f'El promedio de lunas es: {average_moons}')