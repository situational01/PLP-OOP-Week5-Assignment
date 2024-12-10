# Base class representing a generic device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Smartphone class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Calling the constructor of the Device class
        self.storage = storage
        self.battery = battery
    
    # Encapsulated method
    def __battery_status(self):
        return f"Battery: {self.battery}%"

    # Public method
    def details(self):
        return f"Smartphone: {self.info()}, Storage: {self.storage}GB, {self.__battery_status()}"

# Another inherited class with additional behavior
class Smartwatch(Device):
    def __init__(self, brand, model, heart_rate_monitor):
        super().__init__(brand, model)
        self.heart_rate_monitor = heart_rate_monitor
    
    def details(self):
        return f"Smartwatch: {self.info()}, Heart Rate Monitor: {self.heart_rate_monitor}"
    
# Creating instances of Smartphone and Smartwatch
phone = Smartphone("Apple", "iPhone 15", 128, 85)
watch = Smartwatch("Samsung", "Galaxy Watch 6", True)

print(phone.details())
print(watch.details())
