# David Mitchell
# Student ID: 000273705
# WGUPS Package Routing Program

# upon programs launch the program first calls thes functions to load all data from the csv files
# this inserts all package data into a hash table and distance and address data into lists
# the program then asks for a user input time in 24 hour format verifying it is input properly
# If time is after 1020 a function is called to update the package with an incorrect address
# the progarm then calls functions in the following order:
# 1. the function to sort packages by deadline
# 2. the function to load the trucks per the provided notes
# 3. for each truck the function to set the optimal route of the truck using the nearest neighbor algorithm.
# 4. the function to update the status of the trucks and packages at the time provided by the user.
# 5. finally the user interface is called for the user to request information.



import sys
import Packages
import Algorithm
import Destinations
import Truck

Packages.loadPackageData("WGUPS Package File.csv")


# Initializes the program and calls all necessary functions
# first function called by program.
# calls the function to load the hash table for the packages
# Packages.loadPackageData("WGUPS Package File.csv")

# Initializes the user interface calling any functions that need to run upon start up.
# second function called upon starting the program.
def userInterfaceStart():
    print("WGUPS Package Delivery Service.\n")

    # calis time inputfunction to simulate various times of the day to demonstrate fuctionalities of the program
    timeInput()
    
# Takes a user input time, passing that to functions that update both the trucks data as well as the package data in the hash table.
# Finally calls the function for the main user interface
def timeInput():
    print("please Enter the time(24 hour clock format: xxxx): ")
    selection = input()
    try:
        int(selection)
    except ValueError:
        print("please enter a valid time.\n Times must be entered in 24 hour format.\n")
        timeInput()
    if len(selection) != 4:
        print("time must be a four digit number.")
        timeInput()
    elif int(selection) < 800 or int(selection) > 1700:
        print("Time must be between 8:00 am and 5:00 pm.")
        timeInput()
    elif int(selection) >= 1020:
        p = Packages.Package(9, "410 S State St", "Salt Lake City", "UT", 84103, "EOD", 2, "Wrong address listed", "At Hub")
        Packages.packageHash.insert(9, p)
        Algorithm.deadlineList = Algorithm.sortPackagesByDeadline()
        # calls the functions that loads the trucks with packages to be delivered
        Algorithm.loadPackagesPerNotes()
        Truck.truck1 = Truck.prepTruck1()
        Truck.truck2 = Truck.prepTruck2()
        Truck.truck3 = Truck.prepTruck3()
        Truck.updateTrucksAndPackages(selection, Truck.truck1)
        Truck.updateTrucksAndPackages(selection, Truck.truck2)
        Truck.updateTrucksAndPackages(selection, Truck.truck3)
        userInterface()
    elif int(selection) < 1020:
        Packages.loadPackageData("WGUPS Package File.csv")
        Algorithm.deadlineList = Algorithm.sortPackagesByDeadline()
        Algorithm.loadPackagesPerNotes()        
        Truck.truck1 = Truck.prepTruck1()
        Truck.truck2 = Truck.prepTruck2()
        Truck.truck3 = Truck.prepTruck3()
        Truck.updateTrucksAndPackages(selection, Truck.truck1)
        Truck.updateTrucksAndPackages(selection, Truck.truck2)
        Truck.updateTrucksAndPackages(selection, Truck.truck3)
        userInterface()


# the user interface of the program. a simple command line interface.
# takes numbers as arguments and returns requested information.
# called after user input time
def userInterface():
    global time
    print("Please Select an Option:")
    print(
        "   1. Check Truck status\n",
        "   2. Check Package Status\n",
        "   3. Change Time\n",
        "   4. Exit \n",
        sep="",
    )
    selection = input()
    try:
        int(selection)
    except ValueError:
        print("Please enter a valid number.")
        print("\n")
        userInterface()
    if selection == "1":
        print("1. All trucks.\n", "2. Select a truck.\n", "3. Back.\n", sep="")
        selection = input()
        if selection == "1":
            print("Truck 1 status: ")
            Truck.getTruckPackages(Truck.truck1)
            print("Truck 2 status: ")
            Truck.getTruckPackages(Truck.truck2)
            print("Truck 3 status: ")
            Truck.getTruckPackages(Truck.truck3)
            print("Total miles for all trucks: ", (float(Truck.truck1.totalMiles) + float(Truck.truck2.totalMiles) + float(Truck.truck3.totalMiles)))
            userInterface()
        elif selection == "2":
            print("1. Truck 1.\n", "2. Truck 2.\n", "3. Truck 3.\n", ) 
            selection = input()
            if selection == "1":
                print("Truck 1 status: ")
                Truck.getTruckPackages(Truck.truck1)
            if selection == "2":
                print("Truck 2 status: ")
                Truck.getTruckPackages(Truck.truck2)
            if selection == "3":
                print("Truck 3 status: ")
                Truck.getTruckPackages(Truck.truck3)
            userInterface()
        elif selection == "3":
            userInterface()
    elif selection == "2":
        print("1. All Packages.\n", "2. Search by package Id: \n", "3. Back\n", sep="")
        selection = input()
        if selection == "1":
            Packages.getAllPackageData()
            userInterface()
        elif selection == "2":
            print("Please input a package ID: ")
            packageID = input()

            print("package status: ",Packages.getPackageById(packageID))
            print("\n")
            userInterface()
    elif selection =="3":
        timeInput()
    elif selection == "4":
        sys.exit()



userInterfaceStart()

