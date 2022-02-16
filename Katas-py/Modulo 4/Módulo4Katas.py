
#Actividad 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

text.split('.')
print ("¿Existe average?")
print('average' in text)
print ("¿Existe temperature?")
print('temperature' in text)
print ("¿Existe distance?")
print('distance' in text)

for item in text.split('.'):
    if item.find('Moon') > 0:
        value = item.replace('C', 'Celsius')
        print(value)

#Actividad 2
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
#titulo
title = f"""-----------------------------
Gravity Facts about %s
-----------------------------""" % name
#Cuerpo del mensaje
body = f"""Planet Name: {planet}
Gravity on {name} : {gravity * 1000} m/s2"""

#union de titulo y cuerpo
template = f"""{title.title()}
{body}
"""
print (template)

#Nueva información
planet = "Marte"
gravity  = 0.00143
name = "Ganímedes"

print(template)

newTemplate = f"""-----------------------------
Gravity Facts about {name}
-----------------------------
Planet Name: {planet}
Gravity on {name} : {gravity} m/s2
"""

print(newTemplate.format(name=name, gravity=gravity*1000, planet=planet))