# This is where a subclass inherits from a superclass. 
# When this happens, it inherits both the attribute and the behaviors of the superclass.

class Animal:
    alive = True

    def eat(self):
        return "The animal can Eat"

    def runs(self):
        return "The animal can Run"


class Fish(Animal):
    def swims(self):
        return ("The fish can Swim")


class Cow:
    def mooes(self):
        return ("The cow can Moo")


# create an object for the two classes so that you can access either the properties or the behaviours

fish = Fish()
cow = Cow()

# access the property
print(fish.alive)
# access the function
print(fish.swims())  

# multi-level inheritance
class Tilapia(Fish):
    def jump(self):
        return ("The tilapia can jump")
    
Tilapia = Tilapia()

# Testing whether you can access the property alive
print("The tilapia is alive: ",Tilapia.alive)
