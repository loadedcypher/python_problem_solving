# Inheritance 

# A class can inherit attributes from another class.
# A class that is inherited from is called a superclass.
# A class that inherits from another class is called a subclass. 

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grrr......")

# Dog inherits the color and name attributes from Wolf class. 

class Dog(Wolf):
    def bark(self):
        print('woof....')

bull_dog = Dog("Zeus", "Grey")
bull_dog.bark()

husky = Wolf("Fido", "White")
husky.bark()

# Inheritance can also be indirect, one class can inherit from another, and that class can inherit from a third class.

class A:
    def first_method(self):
        print("first method")

class B(A):
    def second_method(self):
        print("second method")

class C(B):
    def third_method(self):
        print("third method")

# C inherits from B which inherits from A, enabling C to inherit all of the attributes of B and A. 

class_3 = C()
class_3.first_method()
class_3.second_method()
class_3.third_method()