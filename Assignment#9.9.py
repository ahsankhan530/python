class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=65):
         self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size==65:
            self.battery_size=85
            print('upgrade the battery to 85 km ')
        else:
            print('the battery is already upgraded')
class ElectricCar(Car):
    def __init__(self, make, model, year):
       super().__init__(make, model, year)
       self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print('\nupgrade the battery')
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()