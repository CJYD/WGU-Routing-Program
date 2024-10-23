import datetime


from Load import package_table
from Deliver import total_mileage


#User Interface
class Main:
    def __init__(self):
        print("WGUPS Routing Program")
        self.show_total_mileage()
        self.start_interface()

    # Display the total mileage for all trucks
    # O(1) time complexity
    def show_total_mileage(self):
        print(f"The total mileage for all trucks: {total_mileage}")

    # Start the user interface
    # O(1) time complexity
    def start_interface(self):
        input("Press Enter to start...")
        self.show_menu()

    # Display menu for the user to choose from
    # O(1) time complexity
    def show_menu(self):
        while True:
            print("\nPlease select an option:")
            print("1. View status of a single package")
            print("2. View status of all packages")
            print("3. View total mileage of all trucks")
            print("4. Exit")
            user_choice = input("\nEnter the number of your choice: ")

            if user_choice == "1":
                self.process_time_input(single_package=True)
            elif user_choice == "2":
                self.process_time_input(single_package=False)
            elif user_choice == "3":
                self.show_total_mileage()
            elif user_choice == "4":
                self.exit_program("\nExiting program. See you next time!")
            else:
                print("Invalid. Please enter a number between 1 and 4.")

    # Process the user time input
    # O(1) time complexity
    def process_time_input(self, single_package):
        try:
            user_time = input("\nPlease enter a time to check the status of a package(s). Use the following format, HH:MM:SS: ")
            status_time = self.change_status(user_time)
            # Update package address
            if status_time >= datetime.timedelta(hours=10, minutes=20):
                self.update_package_address(9, "410 S State St")
            if single_package:
                self.single_package_status(status_time)
            else:
                self.all_packages_status(status_time)
        except ValueError:
            self.exit_program("Invalid time format. Closing Program.")

    # Convert user input time str into timedelta object
    # O(1) time complexity
    def change_status(self, time_str):
        h, m, s = map(int, time_str.split(":"))
        return datetime.timedelta(hours=h, minutes=m, seconds=s)

    def update_package_address(self, package_id, new_address):
        package = package_table.search(package_id)
        package.address = new_address

    #Display status of a single package
    # O(1) time complexity
    def single_package_status(self, time):
        try:
            package_id = int(input("Enter the package ID: "))
            package = package_table.search(package_id)
            package.change_status(time)
            print("\nPackage Status at", time)
            print(f"{'ID':<5} {'Address':<50} {'Deadline':<15} {'Status':<20} {'Delivered At':<20} {'Truck':<6}")
            print("-" * 120)

            if package.status == "Delivered" and package.delivery_time:
                hours, remainder = divmod(package.delivery_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                delivery_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            else:
                delivery_time = "Not delivered"

            print(f"{package_id:<5} {package.address:<50} {package.deadline:<15} "
                  f"{package.status:<20} {delivery_time:<20} {package.truck_id:<6}")
        except (ValueError, KeyError):
            self.exit_program("An error occurred while gathering package information. Closing Program.")

    # Display the status of all packages
    # O(n) time complexity, where n is the total number of packages
    def all_packages_status(self, time):
        try:
            print("\nPackage Status at", time)
            print(f"{'ID':<5} {'Address':<50} {'Deadline':<15} {'Status':<20} {'Delivered At':<20} {'Truck':<6}")
            print("-" * 120)
            for package_id in range(1, 41):
                package = package_table.search(package_id)
                package.change_status(time)
                if package.status == "Delivered" and package.delivery_time:
                    hours, remainder = divmod(package.delivery_time.seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    delivery_time = f"{hours:02}:{minutes:02}:{seconds:02}"

                else:
                    delivery_time = "Not delivered"

                print(f"{package_id:<5} {package.address:<50} {package.deadline:<15} "
                      f"{package.status:<20} {delivery_time:<20} {package.truck_id:<6}")
        except (ValueError, KeyError):
            self.exit_program("An error occurred while gathering package information. Closing Program.")

    # Exit program
    # O(1) time complexity
    def exit_program(self, message):
        print(message)
        exit()

# Initialize the Main class to start the program
Main()


