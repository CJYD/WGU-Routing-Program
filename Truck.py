

# Initializes a new Truck object with the specified attributes
# O(1) time complexity
class Truck:
    def __init__(self, truck_id, capacity, speed, load, packages, mileage, address, depart_time):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    # Returns a string representation of the Truck object
    # O(1) time complexity
    def __str__(self):
        return (f"{self.truck_id}, {self.capacity}, {self.speed}, {self.load}, {self.packages}, "
                f"{self.mileage}, {self.address}, {self.depart_time}")