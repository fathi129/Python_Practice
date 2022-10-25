
class Vehicle:
    def __init__(self,speed,gear):
        self.speed = speed
        self.gear = gear
    def speed1(self):
        print("speed of vehicle is",self.speed)    
    def show(self):
        print("Vehicle has a speed of ",self.speed,"and has",self.gear,"gears.")

class Car(Vehicle):
    def speed1(self):
         print("speed of car is",self.speed)  
    def show(self):
        print("car has a speed of ",self.speed,"and has",self.gear,"gears.")     


vehicle = Vehicle(240,5)
vehicle.speed1()
vehicle.show()

car = Car(450,8)
car.speed1()
car.show()
truck = Vehicle(400,3) 
truck.speed1()
truck.show()
