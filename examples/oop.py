# Abstraction & Encapsulation
class Vehicle:
    def __init__(self, name, speed):
        self.name = name  # Encapsulated Attribute
        self.speed = speed  # Encapsulated Attribute

    def display_info(self):  # Method to display vehicle information
        print(f"Vehicle Name: {self.name}, Speed: {self.speed} km/h")

# Inheritance
class Car(Vehicle):
    def __init__(self, name, speed, wheels):
        super().__init__(name, speed)
        self.wheels = wheels  # New attribute specific to Car

    def display_info(self):  # Overridden method
        super().display_info()
        print(f"It has {self.wheels} wheels.")

# Inheritance
class Boat(Vehicle):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity  # New attribute specific to Boat

    def display_info(self):  # Overridden method
        super().display_info()
        print(f"It has a capacity of {self.capacity} people.")

# Polymorphism in action
def vehicle_details(vehicle):
    vehicle.display_info()  # Polymorphic method call

# Creating instances
car = Car("Ford Mustang", 250, 4)
boat = Boat("Yacht", 30, 10)

# Displaying information
vehicle_details(car)  # Polymorphic behavior
vehicle_details(boat)  # Polymorphic behavior