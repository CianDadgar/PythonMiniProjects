class Car:
    
    def __init__(self, year, make, model):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0

    def set_year(self, year):
        self.__year = year

    def set_make(self, make):
        self.__make = make
        
    def set_model(self, model):
        self.__speed = 0

    def set_speed(self, speed):
        self.__speed = 0

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed +=5

    def brake(self):
        self.__speed -=5

    def get_speed(self):
        return self.__speed

    def __str__(self):
        
        description = input('Enter Make, model and year of car:')
    
        
        return description

def main():
    car = Car("make:","c","3112")
    print(car)
    
    
    speed = "speed of car:"
    a = 0
    while (a < 5):
        car.accelerate()
        print (speed)
        print (car.get_speed())
        a = a + 1
    b = 0
    while (b < 5):
        car.brake()
        print(speed)
        print(car.get_speed())
        b = b + 1
main()
