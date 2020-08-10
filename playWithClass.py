class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initializing The Car"""
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel Tank is full")

    def drive(self):
        """Simulate Driving"""
        print("Car is driving")

    def age(self):
        return "2020 - " + self.year


my_car = Car("audi", "a4", "2016")
print(my_car.make)
print(my_car.model)
print(my_car.year)

my_car.fill_tank()
my_car.drive()
print(my_car.age())
