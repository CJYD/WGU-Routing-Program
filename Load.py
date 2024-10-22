import csv
import datetime

from Data import package_table
from Package import Package
from Truck import Truck


# CSV helper function
def read_csv(filename):
    with open(filename) as csvfile:
        return list(csv.reader(csvfile))

# Using the helper function call for each CSV file
CSV_Package = read_csv("CSV/Package.csv")

# Loads package data from CSV file and inserts each package into a hash table
# O(n) time complexity, where n is the number of packages read from CSV file
def load_package(filename, package_table):
    # open the CSV file containing package details
    with open(filename) as package_details:
        package_data = csv.reader(package_details)
        # Iterate through each row in the CSV file
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = package[6]
            status = "At hub"
            # Create package object
            pkg = Package(package_id, address, city, state, zipcode, deadline, weight, status)
            # Insert the package object into the hash table
            package_table.insert(package_id, pkg)

# Assign packages to truck ID
def assign_packages_to_truck(truck):
    for package_id in truck.packages:
        package = package_table.search(package_id)
        package.truck_id = truck.truck_id
        package.departure_time = truck.depart_time


def initialize_trucks():
    # Create a Truck object representing Truck 1
    truck1 = Truck(1, 16, 18, None, [1, 4, 5, 7, 8, 13, 14, 15, 16, 17, 19, 20, 29, 30, 31, 37, 40],
                         0.0, "4001 South 700 East", datetime.timedelta(hours=8))
    # Create a Truck object representing Truck 2
    truck2 = Truck(2, 16, 18, None, [2, 3, 6, 10, 11, 12, 18, 22, 25, 28, 32, 33, 36, 38],
                         0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
    # Create a Truck object representing Truck 3
    truck3 = Truck(3, 16, 18, None, [9, 21, 23, 24, 26, 27, 34, 35, 39],
                         0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=30))

    # Assign packages to each truck
    assign_packages_to_truck(truck1)
    assign_packages_to_truck(truck2)
    assign_packages_to_truck(truck3)

    # Return the truck objects for processing
    return truck1, truck2, truck3
