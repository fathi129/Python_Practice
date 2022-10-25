class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")  
class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")  
class Sports_car(Car):
    def sports_info(self):
        print("Inside Sports car class.....")  




car = Car()
car.car_info()
car.vehicle_info()
truck = Truck()
truck.truck_info()
truck.vehicle_info()

s = Sports_car()
s.car_info()
s.sports_info()
s.vehicle_info()
