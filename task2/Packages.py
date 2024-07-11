import csv
from Hash import ChainingHashTable

# Hash table instance used for the packages
packageHash = ChainingHashTable(40)

# function initilizes the packages class used across the program for various purposes.
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, specialNotes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.specialNotes = specialNotes
        self.status = status

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.specialNotes, self.status)

# function reads the csv file taking each line as an input for a package object
# the function then passes the object to the hash tables insert function
def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pSpecialNotes = package[7]
            pStatus = "at hub"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZipcode,
                        pDeadline, pWeight, pSpecialNotes, pStatus)
            # print(m)

            # insert it into the hash table
            packageHash.insert(pID, p)


# function retrieves and prints all packages present in the packages Hash table
def getAllPackageData():
    print("all package data: ")
    for i in range(len(packageHash.table)):
        p = packageHash.search(i + 1)
        pID = int((getattr(p, 'ID')))
        pAddress = (getattr(p, 'address'))
        pCity = (getattr(p, 'city'))
        pState = (getattr(p, 'state'))
        pZipcode = (getattr(p, 'zipcode'))
        pDeadline = (getattr(p, 'deadline'))
        pWeight = (getattr(p, 'weight'))
        pSpecialNotes = (getattr(p, 'specialNotes'))
        if pSpecialNotes == '':
            pSpecialNotes = 'N/A'
        pStatus = (getattr(p, 'status'))
        print('Package ID:', pID, '| Address:', pAddress, '| City:', pCity, '| State:', pState, '| Zipcode:', pZipcode,
              '| Deadline:', pDeadline, '| weight:', pWeight, '| special Notes:', pSpecialNotes, '| Status:', pStatus)

# function takes a package ID as an argument and returns the selected package from the hash table
def getPackageById(packageID):
    # print("Package Data: ")
    p = packageHash.search(int(packageID))
    pID = int((getattr(p, 'ID')))
    pAddress = (getattr(p, 'address'))
    pCity = (getattr(p, 'city'))
    pState = (getattr(p, 'state'))
    pZipcode = (getattr(p, 'zipcode'))
    pDeadline = (getattr(p, 'deadline'))
    pWeight = (getattr(p, 'weight'))
    pSpecialNotes = (getattr(p, 'specialNotes'))
    if pSpecialNotes == '':
        pSpecialNotes = 'N/A'
    pStatus = (getattr(p, 'status'))
    package = ['Package ID:', pID, '| Address:', pAddress, '| City:', pCity, '| State:', pState, '| Zipcode:', pZipcode,
          '| Deadline:', pDeadline, '| weight:', pWeight, '| special Notes:', pSpecialNotes, '| Status:', pStatus]
    return package
