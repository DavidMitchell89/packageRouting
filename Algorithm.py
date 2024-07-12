# algorithm.py serves as the module for implementing the next nearest neighbor algorithm implemented in this program
# the algorithm utilizes the setOptimalRoute function for the primary sorting, which utilizes several other smaller functions to look and find other necessary information 

import Packages
import Destinations
from operator import itemgetter

packagesForTruck1 = [13, 14, 15, 16, 19, 20]
packagesForTruck2 = [3, 18, 36, 38, 6, 9, 25, 28, 32]

truckList1 = []
truckList2 = []
truckList3 = []

packagesPlacedOnTrucks = []

deadlineList = []

# Calls function to load package data from csv file.
# Packages.loadPackageData("WGUPS Package File.csv")


# function takes packages from the hash table and passes them into a transformable list
# then calls pythons proprietary sort algorithm to sort the packages by deadline
# function is called immediately after the function to load packages from the csv file
# complexity (0(n^2))
def sortPackagesByDeadline():
    # print(len(Packages.packageHash.table))
    deadlineList.clear()
    for i in range(len(Packages.packageHash.table)):
        p = Packages.packageHash.search(i + 1)
        pID = str(getattr(p, "ID"))
        pAddress = str(getattr(p, "address"))
        location = ""
        for sublist in Destinations.addressTable:
            if sublist[1] == pAddress:
                location = str(sublist[0])
        # print(location)
        pDeadline = getattr(p, "deadline")
        pStatus = getattr(p, "status")
        pListObj = (
            "Package ID",
            pID,
            "Location:",
            location,
            "Address:",
            pAddress,
            "Deadline:",
            pDeadline,
            "status:",
            pStatus,
        )
        deadlineList.append(pListObj)
    sortedByDeadline = sorted(deadlineList, key=itemgetter(7))
    # print(*sortedByDeadline, sep="\n")
    return sortedByDeadline


# ensures deadline list has been set and sorted appropriately
# deadlineList = sortPackagesByDeadline()

# This function is called immediately after the package sort function.
# Places packages on the trucks first by stated requirements(packages that must be delivered together or on a specific truck)
# finally places reamaining packages on trucks 1 and 2 until they reach 15 packages each
# remainging packages are placed on truck 3
def loadPackagesPerNotes():
    packagesPlacedOnTrucks.clear()
    truckList1.clear
    truckList2.clear
    truckList3.clear
    for package in deadlineList:
        # print(package)
        if package not in packagesPlacedOnTrucks:
            if int(package[1]) in packagesForTruck1:
                # print("package for truck 1")
                truckList1.append(package)
                packagesPlacedOnTrucks.append(package)
                # print("Truck 1: ")
                # print(*truckList1, sep="\n")
            elif int(package[1]) in packagesForTruck2:
                # print("package for truck 2")
                truckList2.append(package)
                packagesPlacedOnTrucks.append(package)
                # print("Truck 2:")
                # print(len(sortedDeadlineList))
                # print(*truckList2, sep="\n")
    for package in deadlineList:
        if package not in packagesPlacedOnTrucks:
            if len(truckList1) < 15:
                truckList1.append(package)
                packagesPlacedOnTrucks.append(package)
            elif len(truckList2) < 15:
                truckList2.append(package)
                packagesPlacedOnTrucks.append(package)
            elif len(truckList3) < 14:
                truckList3.append(package)
                packagesPlacedOnTrucks.append(package)
        # print("packages on trucks:")
    # print(*truckList1, sep="\n")

shortestDistance = []
optimalRoute1 = []
optimalRoute2 = []
optimalRoute3 = []

# function to return the distance between two given locations
# first references the address table for the locations index
# then uses the index numbers on the distance table as cross reference numbers to retrieve the distance
# function is called as part of other functions
def getDistance(address1, address2):
#     print(address1, address2)
    start = 0
    end = 0
    start = Destinations.deepindex(Destinations.addressTable, address1)
    end = Destinations.deepindex(Destinations.addressTable, address2)
    distance = Destinations.distanceTable[start][end]
    return distance

# function to find the package on a truck nearest the hub
# checks the distance from the hub for each package
# appends the distance to a list
# returns package with shortest distance
def getNearestToHub(list):
#     print(*list, sep="\n")
    pointA = "Western Governors University"
    distance = 0.0
    nextStop = ""
    for i in list:
        shortestDistance.append(float(getDistance(pointA, i[3])))
        distance = min(shortestDistance)
    for i in list:
        if distance == float(getDistance(pointA, i[3])):
            nextStop = i
    shortestDistance.clear()
    return nextStop

# function serves as a piece of the next nearest neighbor algorithm implemented in thes program
# takes the current package and searches the still unsorted list of packages on a truck and returns the package closest to the current package
def getNextStop(list, route, previousStop):
# #     print("previous Stop: ", previousStop)
    distance = 0.0
    nextStop = []
    for i in list:
# #         # print("i: ", i)
        if i[3] != previousStop and not any(i[3] in j for j in route):
# #             # print("route")
# #             # print(*route, sep="\n")
# #             # print("i3 and previous stop: ", i[3], previousStop)
            shortestDistance.append(float(getDistance(previousStop, i[3])))
# #             # print("shortestDistance", *shortestDistance, sep="\n")
            distance = min(shortestDistance)
    for i in list:
        if i[3] != previousStop and not any(i[3] in j for j in route):
# #             # print(previousStop)
            if distance == float(getDistance(previousStop, i[3])):
                if len(nextStop) == 0:
                    nextStop.append(i)
                elif len(nextStop) > 0:
                    if i[3] == nextStop[0][3]:
                        nextStop.append(i)
    shortestDistance.clear()
# #     print(*nextStop, sep="\n")
    return nextStop

# accessory function to flatten a list of lists
# used to appropriately append information during the nearest neighbor algorithms sorting process
def flattenList(list):
    flatList = []
    for subList in list:
        flatList += subList
    return flatList
    
# The main function in the Next Nearest neighbor aglorithm being implemented
# function takes the list of packages placed on a truck and first finds the first stop, the package address nearest to the hub
# the function then appends the distance from the hub to the address to the truck list for later reference
# second, starting with the first stop address it calls the getNextStop function to find the next nearest address
# the function adds the distance to this next address to the distance appended to the previous address and appends it to the current address for future reference
# the function repeats this process until all packages have been sorted in this manner
# the function finally removes any duplicates that may have ended up on the list
def setOptimalRoute(list, route):
    route.clear()
    addressToAppend = ""
    distance = 0.0
    for i in range(len(list)):
        firstStop = getNearestToHub(list)
        if len(route) == 0:
#     #         # print("OR \n", len(route))
#     #         # print("first stop: \n", firstStop)
#     #         # print("distance: ", getDistance("Western Governors University", firstStop[3]))
            distance = float(getDistance("Western Governors University", firstStop[3]))
#     #         # print(distance)
            route.append(flattenList([["distance:"], [str(distance)], firstStop]))
        elif len(route) == 1:
#     #         # print("OR \n", len(route))
            addressToAppend = getNextStop(list, route, firstStop[3])
#     #         # print("Address to append: ")
#     #         # print(*addressToAppend, sep="\n")
#     #         # print("distance between: ", firstStop[3], addressToAppend[0][3])
#     #         # print("distance: ", getDistance(firstStop[3], addressToAppend[0][3]))
            distance = distance + float(getDistance(firstStop[3], addressToAppend[0][3]))
#     #         print(addressToAppend[0][3])
            for i in range(len(addressToAppend)):
                route.append(flattenList([["distance:"], [str(distance)], addressToAppend[i]]))
        elif len(route) >= 2:
#     #         # print("OR \n", len(route))
            addressToAppendL = getNextStop(list, route, addressToAppend[0][3])
#     #         # print("Address to append: ")
#     #         # print(*addressToAppendL, sep="\n")
            if len(addressToAppendL) == 0:
#     #             print(route[-1][5])
                distance = distance + float(getDistance("Western Governors University", route[-1][5]))
                route.append(["distance:", str(distance),
                             "Package ID:", "0",
                             "location:", "Western Governors University",
                             "Address:", "4001 South 700 East",
                             "Deadline:", "N/A",
                             "status:", "hub"])
                return
#     #         # print("distance between: ", addressToAppend[0][3], addressToAppendL[0][3])
#     #         # print("distance: ", getDistance(addressToAppend[0][3], addressToAppendL[0][3]))
            distance = distance + float(getDistance(addressToAppend[0][3], addressToAppendL[0][3]))
#     #         # print(distance)
            for i in range(len(addressToAppendL)):
                route.append(flattenList([["distance:"], [str(distance)], addressToAppendL[i]]))
            addressToAppend = addressToAppendL
#     #         # print(addressToAppendL)
#     #         print("OR: ", len(route), "\n", "list: ", len(list))
    res = [i for n, i in enumerate(route) if i not in route[:n]]
#     # # print(*res, sep="\n")
    return res
