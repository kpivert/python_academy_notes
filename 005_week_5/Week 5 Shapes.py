##############################
# An OOP crash course :)
##############################

############################################################
# SIMPLE RECTANGLE CLASS
# with 2 attributes:  width, height
############################################################
class Rectangle:
    
    #A Rectangle has 2 attributes:  width, height
    def __init__(self, width, height):  #Constructor that will be called to initialize/create the object/instance
        self.width = width
        self.height = height

    @property  #properties feel like attributes but aren't
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    #A regular utility method that will be built into every instance
    def is_square(self):
        return self.width == self.height

    @staticmethod  #A Static/class method doesn't require "state" information, ie, 
                   #the attribute information that "lives inside of" each object.
                   #So this square method is given the side_length and doesn't depend on
                   #the height/width attributes from a Rectangle object.
    def square(side_length):
        return Rectangle(side_length, side_length)

    @staticmethod
    def unit_square():
        return Rectangle(1, 1)

    #__str is the friendly, human-readable string representation of an object.
    #For exmaple, this method is called when you use print(XXX) --> So the __str__ function 
    #associated with XXX gets called.
    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}, area={self.area:.2f}, perimeter={self.perimeter:.2f}"

    #__repr__ is more for debugging/coders but the idea is similar to __str__
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


############################################################
# Example of why you see __name__ in code sometimes
############################################################

print(__name__)  #This variable is set to "__main__" 
                 #     when running this file directly as a script.
                 #It is set to "shapes" when this file is imported into another file.

if __name__ == "__main__":  #So if I'm running this file directly as a script, 
                            #the code in this if-statement will run. 
                            #For any files that import this shapes file as a module 
                            #the block of code in this if statement would be skipped.
    r = Rectangle(1,2)
    print(r)

##############################
# TRIANGLE CLASS
##############################
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return 0.5 * self.base * self.height

    @staticmethod
    def area_from_sides(a, b, c):
        """Create a Triangle using Heron’s formula (area from three sides)."""
        # semi-perimeter
        s = (a + b + c) / 2
        area =  (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

    def __str__(self):
        return f"Triangle with base={self.base} and height={self.height}, area={self.area}"

    def __repr__(self):
        return f"Triangle(base={self.base}, height={self.height})"
