def reportTanks(valueTank1, valueTank2, valueTank3):
    AverageValueTank = (valueTank1 + valueTank2 + valueTank3) / 3
    return f"""
    El reporte de los tanque de combustible:
    El tanque 1 tiene: {valueTank1} % de combustible
    El tanque 2 tiene: {valueTank2} % de combustible
    El tanque 3 tiene: {valueTank3} % de combustible
    El promedio de combustible: {AverageValueTank} %
    """
print(reportTanks(10,10,10))

def averageFuel(valuesTanks):
    totalFuel = sum(valuesTanks)
    tanksTotalItems = len(valuesTanks)
    response = totalFuel / tanksTotalItems
    return response

averageFuel([10,10,10])

def reportTanks(valueTank1, valueTank2, valueTank3):
    AverageValueTank = averageFuel([valueTank1, valueTank2, valueTank3])
    return f"""
    El reporte de los tanque de combustible:
    El tanque 1 tiene: {valueTank1} % de combustible
    El tanque 2 tiene: {valueTank2} % de combustible
    El tanque 3 tiene: {valueTank3} % de combustible
    El promedio de combustible: {AverageValueTank} %
    """
print(reportTanks(10,10,10))

# Ejercicio 2

def reportMision(timePreLaunch, timeFly, destination, valueTankExt, valueTankInt):
    return f"""
    El reporte de la misión:
    La hora de prelazanmiento: {timePreLaunch} minutos
    El tiempo de misión: {timePreLaunch + timeFly} minutos
    El destino es: {destination}
    El total de combustible: {valueTankExt + valueTankInt} Toneladas
    """
print(reportMision(50,2500,'Marte',120,50))

def reportMision(destination, *timesMision,  **fuelTanksSet):
    return f"""
    El destino de la misión es {destination}
    El tiempo total del viaje es: {sum(timesMision)} minutes
    Total de combustible de la misión: {sum(fuelTanksSet.values())} Toneladas
    """

print(reportMision("Marte", 23, 27, 50, Interno=50, externo1=60, externo2=60))

def reportMision(destination, *timesMision,  **fuelTanksSet):
    responseReport = f"""
    El destino de la misión es {destination}
    El tiempo total del viaje es: {sum(timesMision)} minutes
    Total de combustible de la misión: {sum(fuelTanksSet.values())} Toneladas
    """
    for tankName, amountTank in fuelTanksSet.items():
        responseReport += f"tanque: {tankName}  cantidad: {amountTank} Toneladas de combustible \n"
    return responseReport

print(reportMision("Marte", 23, 27, 50, Interno=50, externo1=60, externo2=60))