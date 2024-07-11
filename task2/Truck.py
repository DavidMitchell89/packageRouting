import Destinations
import Algorithm
import Packages

Algorithm.loadPackagesPerNotes()
Destinations.populateDistanceTable()
Destinations.populateAddressTable()

rate = 18.0

# initializes the truck class used across the project
# defines all traits needed for the trucks
class Truck:
    # 0(1) constant
    def __init__(
        self,
        location,
        departTime,
        totalMiles,
        totalRouteMiles,
        packagesList,
        packagesNum,
    ):
        self.location = location
        self.departTime = departTime
        self.totalMiles = totalMiles
        self.totalRouteMiles = totalRouteMiles
        self.packagesList = packagesList
        self.packagesNum = packagesNum

# Initializes initial truck values
locationT1 = "at hub"
locationT2 = "at hub"
locationT3 = "at hub"
departTimeT1 = "0800"
departTimeT2 = "1030"
departTimeT3 = "915"
totalMilesT1 = 0
totalMilesT2 = 0
totalMilesT3 = 0
totalRouteMilesT1 = 0
totalRouteMilesT2 = 0
totalRouteMilesT3 = 0
packagesListT1 = []
packagesListT2 = []
packagesListT3 = []
packagesNumT1 = 0
packagesNumT2 = 0
packagesNumT3 = 0

packageList = []

truck1 = Truck(
        location = locationT1,
        departTime = departTimeT1,
        totalMiles = totalMilesT1,
        totalRouteMiles = totalRouteMilesT1,
        packagesList = packagesListT1,
        packagesNum = packagesNumT1
)

truck2 = Truck(
        location = locationT2,
        departTime = departTimeT2,
        totalMiles = totalMilesT2,
        totalRouteMiles = totalRouteMilesT2,
        packagesList = packagesListT2,
        packagesNum = packagesNumT2
)

truck3 = Truck(
        location = locationT3,
        departTime = departTimeT3,
        totalMiles = totalMilesT3,
        totalRouteMiles = totalRouteMilesT3,
        packagesList = packagesListT3,
        packagesNum = packagesNumT3
)

# function to prepare the first truck for departure.
# calls the set optimal route function, and passes the resulting list to the Truck1 class objects package list attribute
def prepTruck1():
    Algorithm.optimalRoute1.clear()
    Algorithm.setOptimalRoute(Algorithm.truckList1, Algorithm.optimalRoute1)
    truck1 = Truck(
            location = locationT1,
            departTime = departTimeT1,
            totalMiles = totalMilesT1,
            totalRouteMiles = totalRouteMilesT1,
            packagesList = Algorithm.optimalRoute1,
            packagesNum = packagesNumT1
    )
    # print(*truck1.packagesList, sep="\n")
    return truck1

# function to prepare the first truck for departure.
# calls the set optimal route function, and passes the resulting list to the Truck2 class objects package list attribute
def prepTruck2():
    Algorithm.optimalRoute2.clear()
    Algorithm.setOptimalRoute(Algorithm.truckList2, Algorithm.optimalRoute2)
    truck2 = Truck(
            location = locationT2,
            departTime = departTimeT2,
            totalMiles = totalMilesT2,
            totalRouteMiles = totalRouteMilesT2,
            packagesList = Algorithm.optimalRoute2,
            packagesNum = packagesNumT2
    )
    # print("Truck 2 List:")
    # print(*truck2.packagesList, sep="\n")
    return truck2

# function to prepare the first truck for departure.
# calls the set optimal route function, and passes the resulting list to the Truck3 class objects package list attribute
def prepTruck3():
    Algorithm.optimalRoute3.clear()
    Algorithm.setOptimalRoute(Algorithm.truckList3, Algorithm.optimalRoute3)
    truck3 = Truck(
            location = locationT3,
            departTime = departTimeT3,
            totalMiles = totalMilesT3,
            totalRouteMiles = totalRouteMilesT3,
            packagesList = Algorithm.optimalRoute3,
            packagesNum = packagesNumT3
    )
    return truck3


     
# function calculates the time truck has spent traveling since its depart time
# the function first checks that the user input time is in an appropriate format
# finally transforms the 24 hour time used and combines the two times into a resulting decimal time.
# the function is used in the function to update the truck and package data at a given time of day.
def calculateTravelTime(departTime, currentTime):
    tempTime = int(currentTime) - int(departTime)
    # print("org time", tempTime)
    if str(tempTime)[-2:] >= "60":
        tempTime = tempTime - 40
    if tempTime < 100:
        travelTime = tempTime/60
    #     print(travelTime)
    elif tempTime >= 100:
    #     print("chg time", tempTime)
        tempHrs = int(str(tempTime)[0])
    #     print("hrs", tempHrs)
        tempMin = int(str(tempTime)[1:])/60
    #     print("mins", tempMin)
        travelTime = float(tempHrs + tempMin)
    #     print(travelTime)
    return travelTime

# function calculates the time that the package was delivered
# calculates how for the address is, in minutes, from the hub along the set route
# adds that time to the depart time to get the time of delivery for the package 
def deliveryTime(truck, distance):
    timeFromDepart = (float(distance) / rate) * 60
    # print("minutes traveled", timeFromDepart)
    if timeFromDepart >= 60:
        timeFromDepart = timeFromDepart + 40
    # print("changed minutes", timeFromDepart)
    # print("truck depart", truck.departTime)
    # print("deliver Time", timeFromDepart + float(truck.departTime))
    deliverTime = round(timeFromDepart + float(truck.departTime))
    # print("deliver time:", deliverTime)
    if str(deliverTime)[-2:] >= "60":
        deliverTime = deliverTime + 40
    delivery = "Delivered at " + str(round(deliverTime))
    return delivery

# function updates the information on the truck and the package hash table based on given time
# first checks that the user provided time is in an appropriate 24 hour clock format
# then compares the time to the trucks depart time if time is after trucks depart time, truck location is set to "out on delivery"
# the function then compares the distance traveled by the truck to the distance from the hub for each package
# and the packages status is updated appropriately, both on the trucks route list as well as the hash table
def updateTrucksAndPackages(time, truck):
    # print(time)
    if time[-2:] >= "60":
        adjustedTime = int(time) + 40
        # print("adjusted time: ", adjustedTime)        
        time = str(adjustedTime)
    if time > truck.departTime:
        truck.location = "out on delivery"
    distanceTraveled = float(rate * calculateTravelTime(truck.departTime, time))
    # print("Time traveled: ", calculateTravelTime(truck.departTime, time))
    # print("Distance traveled: ", distanceTraveled)
    # print(truck.packagesList[-2][1])
    if distanceTraveled > float(truck.packagesList[-2][1]):
        truck.totalMiles = truck.packagesList[-2][1]
    elif distanceTraveled < 0:
        truck.totalMiles = 0
    else:
        truck.totalMiles = distanceTraveled
    for package in truck.packagesList[:-1]:
        # print(package[1])
        tempPackage = Packages.getPackageById(package[3])
        # print("temp package",tempPackage)
        if float(distanceTraveled) > float(package[1]):
            # print("package", package[3], float(package[1]))
            # print("Delivered at: ", deliveryTime(truck, package[1]))    
            p = Packages.Package(tempPackage[1], str(tempPackage[3]), str(tempPackage[5]), str(tempPackage[7]), str(tempPackage[9]), tempPackage[11], tempPackage[13], tempPackage[15], deliveryTime(truck, package[1]))
            Packages.packageHash.insert(tempPackage[1], p)
            package[-1] = deliveryTime(truck, package[1])
        if float(distanceTraveled) < float(package[1]) and float(distanceTraveled) > 0:
            p = Packages.Package(tempPackage[1], str(tempPackage[3]), str(tempPackage[5]), str(tempPackage[7]), str(tempPackage[9]), tempPackage[11], tempPackage[13], tempPackage[15], "en route")
            Packages.packageHash.insert(tempPackage[1], p)
            package[-1] = "en route"

            
# function used to print the package list of a given truck and its currently driven miles
def getTruckPackages(truck):
    print("Distance Traveled by truck: ", (truck.totalMiles))
    # print(truck.packagesList[:-1][2:], sep="\n")
    trucklist = []
    for package in truck.packagesList[:-1]:
        trucklist.append(package[2:])
    res = [i for n, i in enumerate(trucklist) if i not in trucklist[:n]]
    print(*res, sep="\n")

# Algorithm.loadPackagesPerNotes
# print(Packages.getPackageById(31))
# truck1 = prepTruck1()
# print("Truck 1 before ", *truck1.packagesList[:-1], sep="\n")
# updateTrucksAndPackages("1100", truck1)
# print(Packages.getPackageById(31))
# print("truck 1 after",*truck1.packagesList, sep="\n")
# print(deliveryTime(truck1, 20))
# getTruckPackages(truck1)
