#object oriented programming concepts

class Dog:
    #attributes
    attr1 = "Sheru"
    attr2 = "dog"
    legs = 4
    tail = 1
    #methods
    def fun(self):
        print("I am", self.attr1)
        print("I am a", self.attr2)
#creating the object
Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()

class Jeep:
    jeep_type = "Willys Wrangler"
    attr1 = "Automatic"
    attr2 = "Hybrid Engine"
    color = "Anvil Grey"
    wheels = 4
    seat_texture = "Cloth"
    seats = 4
    # methods
    def write(self):
        print("I am a", self.attr1, "car")
        print("I have a", self.attr2)
# object creation
Car = Jeep()
print(Car.jeep_type)
Car.write()
