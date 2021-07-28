class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

#print(rect.area())

'''
class Square(Rectangle):

    def __init__(self, x):
        Rectangle.__init__(self, x, x)
'''

class Square(Rectangle):

    def __init__(self, x):
        super().__init__(x, x)
        # don't put self because self will be reference itself, and not the rectangle above 

    


newSquare = Square(8)

print(newSquare.area())
print(newSquare.perimeter())
# We have a parent class Rectangle with an area function and a perimeter function
# We have a child class Square that inherits Rectangle self.width;, and self.length
# super allows the child class to access the parent classes methods and properties
# in line 20, super passes length and length to rectangle's __init__ method which will handle them as arguments
# ergo all you did was assign square's length as rectangle's length and rectangle's width 


