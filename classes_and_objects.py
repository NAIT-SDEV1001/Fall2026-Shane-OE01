#Object oriented programming(OOP)
#uses classes(blueprints) to model real world objects/concept
#We instantiate objects from the class and work with the objects
#Each object has its own copy of the attributes

class Car:
    #constructor Method
    #called __init__ and executes when you instantite an object
    #self must be the first parameter in every method. It means "the current object"
    def __init__ (self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0 

    def Honk(self):
        print(f'{self.make}, {self.model} says Beep Beep')

    def Accelerate(self, amount):
        self.speed += amount

    def Decelerate(self,amount):
        self.speed -= amount
    #str dunder method (double underscore)
    def __str__(self):
        return f'This car is a {self.color} {self.year} {self.make}, {self.model}!'

    def __repr__(self):
        #!r will place quotes around the string. 
        return f"Car({self.make!r},{self.model!r},{self.year},{self.color!r})"

def main():
    #create a car object called car1
    #pass in the values for the constructor
    car1 = Car('Ford','F150',2020,'black')
    car2 = Car('Buick','Skylark',1965,'red')
    car3 = Car('Chevy','impala',2006,'purple')

    print (car1.make)
    print (car1.model)

    print (car2.make)
    print (car2.model)

    #change attribute values
    car1.model = 'focus'
    print (car1.model)

    #In Python you can add attributes to objects
    car3.seats = 4
    print(car3.seats)

    #calling methods
    car1.Honk()
    car2.Honk()

    #accelerate
    car2.Accelerate(200)
    print(car2.speed)
    car2.Accelerate(50)
    print(car2.speed)
    car2.Decelerate(200)
    print(car2.speed)
    
    #what happens if you print an object
    #prints the memory location. Useless info

    print (car2)
    print(repr(car2))



if __name__ == '__main__':
    main()
