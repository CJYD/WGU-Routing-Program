import csv
import datetime


from Load import package_table, load_package, initialize_trucks


# CSV helper function
def read_csv(filename):
    with open(filename) as csvfile:
        return list(csv.reader(csvfile))

# Using the helper function call for each CSV file
CSV_Distance = read_csv("CSV/Distance.csv")
CSV_Address = read_csv("CSV/Address.csv")
CSV_Package = read_csv("CSV/Package.csv")

# Calculate the mileage between two distances
# O(1) time complexity
def mileage_between(loc1, loc2):
    distance = CSV_Distance[loc1][loc2].strip()
    return float(distance) if distance else 0.0

# Find the corresponding address in the CSV file
# O(n) time complexity, where n is the number of rows in the CSV file
def get_address(address):
    for row in CSV_Address:
        if address.strip() == row[2].strip():
            return int(row[0])

# Deliver packages for a given truck
# O(n^2) time complexity, where n is the number of packages on the truck.
# The 1st iteration is O(n) + O(n) for finding and removing the nearest package
# The 2nd iteration is O(n-1) + O(n-1)...
# This results in a O(n^2) time complexity for the repeated find and removal operations
def deliver_packages(truck):
    # Retrieve packages that are not yet delivered
    not_delivered = [package_table.search(package_id) for package_id in truck.packages]
    truck.packages.clear()

    # Continue delivering packages until all are delivered
    while not_delivered:
        next_package, next_address = find_next_package(truck, not_delivered)

        # Add the next package to the truck
        truck.packages.append(next_package.id)
        not_delivered.remove(next_package)
        truck_status(truck, next_package, next_address)

# Finds the next package to be delivered by the truck
# O(n) time complexity, where n is the number of packages in not delivered list
def find_next_package(truck, not_delivered):
    next_package = min(
        not_delivered,
        key=lambda package: mileage_between(
            get_address(truck.address),
            get_address(package.address)
        )
    )
    # Calculate distance between the truck's current address the next package address
    next_address = mileage_between(
        get_address(truck.address),
        get_address(next_package.address)
    )
    return next_package, next_address

# Updates the truck's status
# O(1) time complexity
def truck_status(truck, package, distance):
    # Add the distance traveled to the truck's total mileage
    truck.mileage += distance
    # Update the truck's current address to the next package address
    truck.address = package.address
    # Update truck's time by adding the time taken to travel / 18 mph
    truck.time += datetime.timedelta(hours=distance / 18)
    # Set the package delivery time to truck's updated time
    package.delivery_time = truck.time
    # Set the package's departure time to the truck's departure time
    package.departure_time = truck.depart_time

# Load the package data from CSV file
load_package("CSV/Package.csv", package_table)

truck1, truck2, truck3 = initialize_trucks()

# Start delivering packages
deliver_packages(truck1)
deliver_packages(truck2)
# Departure time for Truck 3 to the earlier of Truck 1 or Truck 2 completion time
truck3.depart_time = min(truck1.time, truck2.time)
deliver_packages(truck3)

# Calculate the total mileage traveled by all trucks
total_mileage = truck1.mileage + truck2.mileage + truck3.mileage