# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name+ "is now sitting")
#
#     def roll_over(self):
#         print(self.name + 'rolling')
#
#
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def description(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#
# my_new_car = Car('audi','a4',2016)
# print(my_new_car.description())

# 9-4
# class Restaurant():
#     # 创建一个饭馆的类
#
#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         msg = self.name + " serves wonderful " + self.cuisine_type + "."
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         msg = self.name + " is open. Come on in!"
#         print("\n" + msg)
#
#     def number_served(self,number):
#         self.number = number
#
#     def increase_number(self,addition):
#         self.number += addition
#
# restaurant = Restaurant('the mean queen', 'pizza')
# restaurant.describe_restaurant()
#
# print("\nNumber served: " + str(restaurant.number_served))
# restaurant.number = 430
# print("Number served: " + str(restaurant.number))
#
# restaurant.number_served(1257)
# print("Number served: " + str(restaurant.number))
#
# restaurant.increase_number(239)
# print("Number served: " + str(restaurant.number))

#9-5
#
# class User():
#
#     def __init__(self, first_name, last_name, username, email, location):
#         # 初始化用户
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         print("\nWelcome back, " + self.username + "!")
#
#     def increment_login_attempts(self):
#         self.login_attempts+=1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
#
# eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.greet_user()
#
# print("\nMaking 3 login attempts...")
# eric.increment_login_attempts()
# eric.increment_login_attempts()
# eric.increment_login_attempts()
# print("  Login attempts: " + str(eric.login_attempts))
#
# print("Resetting login attempts...")
# eric.reset_login_attempts()
# print("  Login attempts: " + str(eric.login_attempts))



#9-3 继承

#exercise 9-6
# class Restaurant():
#     # 创建一个饭馆的类
#
#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         msg = self.name + " serves wonderful " + self.cuisine_type + "."
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         msg = self.name + " is open. Come on in!"
#         print("\n" + msg)
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self,name, cuisine_type = 'ice cream'):
#         super().__init__(name,cuisine_type)
#         self.flavours = []
#
#     def show_flavours(self):
#         print("we have following flavours, ")
#         for f in self.flavours:
#             print("-"+f.title())
#
#
# ice_cream = IceCreamStand("ICE CREAM")
# ice_cream.flavours = ['vanilla','chocolate','coffee']
# ice_cream.describe_restaurant()
# ice_cream.show_flavours()

#9-7
# class User():
#
#     def __init__(self, first_name, last_name, username, email, location):
#         # 初始化用户
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         print("\nWelcome back, " + self.username + "!")
#
# class Admin(User):
#     def __init__(self, first_name, last_name, username, email, location):
#         super(Admin, self).__init__( first_name, last_name, username, email, location)
#         self.privileges = []
#
#     def show_priviledges(self):
#         for p in self.privileges:
#             print('The privilege is: '+p)
#
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.privileges = ['can add post','can delete post','can ban user']
# eric.show_priviledges()

#9-9
class Car():

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print("upgrade to 85")

        else:
            print("already upgraded")

class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()