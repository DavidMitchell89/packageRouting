# destinations table
import csv

# Initialization
# get raw data from distance csv
# O(N) linear
distanceTable = []
addressTable = []

# function to read the csv file that contains the distances between all locations
# places distances in a list of lists. to used in the main algorithm
def populateDistanceTable():
    with open("DistanceTable.csv", "r") as read:
        distanceTable = list(csv.reader(read, delimiter=","))
    return distanceTable

# function to read the csv file that contains the addresses of all locations
# places addresses in a list of lists. to used in the main algorithm
def populateAddressTable():
    with open("Addresses.csv", "r") as read:
        addressTable = list(csv.reader(read, delimiter=","))
    return addressTable

# function used to retrieve the index in a list of an object contained in a nested list
# used as part of the get distance function, to get the index of the two locations
def deepindex(lst, w):
    for i, sub in enumerate(lst):
        if w in sub:
            return int(i)


addressTable = populateAddressTable()
distanceTable = populateDistanceTable()
