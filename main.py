from read.py import read_file
#############################Variables##########################################
inputFile = ""
################################################################################
normalizedInput = read_file(inputFile)
#Create and Sort list of rides
listOfRides = normalizedInput.rides
#Sort list by earlier start
listOfRides.sort(key = lambda x : x.earlier_start)
#Create list of vehicules
listOfVehicules = [Vehicule(i) for i in range (normalizedInput.F)]

for ride in listOfRides:
    minIndex = 0
    minimum = listOfVehicules[0].time_for_ride()
    for i in range(1,len(listOfVehicules)):
        currentValue = listOfVehicules[i].time_for_ride(ride)
        if currentValue < minimum:
            minIndex = i
            minimum = currentValue
    listOfVehicules[i].add_trajet(ride)
