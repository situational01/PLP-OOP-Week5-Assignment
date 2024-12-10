# Base class for vehicles
class Vehicle:
    def move(self):
        pass  # To be overridden in each specific class

# Derived class for Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived class for Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived class for Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
