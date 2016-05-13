

## Make a class named Animal that is-a object.
class Animal(object):
    pass
## Make a class name Dog that is-a Animal. 	
class Dog(Animal):
    def __init__(self, name): ## Class Dog has-a __init__  that takes self and name as parameters 
        self.name = name
## is-a
class Cat(Animal):  
    def __init__(self, name): ## has-a
        self.name = name
 
## is-a
class Person(object):
    
    def __init__(self, name):
        self.name = name
    self.pet = None 
## Person has-a pet of some kind   

class Employee(Person):
    def __init__(self, name, salary):
        ##?? hmm what is a strange magic?
        super(Employee, self).__init__(name)
        ## has-a 		
        self.salary = salary	
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibout(Fish):
    pass

rover = Dog("Rover") ## set rover to an instance of class Dog with parameter "Rover". 

satan = Cat("Satan") 

mary = Person("Mary")

mary.pet = satan ## From mary get pet attribute and set it to satan

frank = Employee("Frank", 120000) ## set frank to an instance of class Employee with parameters "Frank" and 120000
frank.pet = rover

flipper = Fish() ## set flipper to an instance of class Fish


crouse = Salmon()

harry = Halibout()
	
    		