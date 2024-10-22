# Initializes a new Package object with the specified attributes
# O(1) time complexity
class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status, truck_id=None):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.truck_id = truck_id

    # Returns a string representation of the Package object
    # O(1) time complexity
    def __str__(self):
        return (f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zipcode}"
                f"{self.deadline}, {self.weight}, {self.delivery_time}, {self.status}, {self.truck_id}")

    # Updates the package's status based on the provided time
    # O(1) time complexity
    def change_status(self, current_status):
        if self.delivery_time < current_status:
            self.status = "Delivered"
        elif self.departure_time > current_status:
            self.status = "En route"
        else:
            self.status = "At hub"


    def set_truck_id(self, truck_id):
        self.truck_id = truck_id