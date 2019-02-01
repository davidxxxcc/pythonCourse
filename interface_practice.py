# Abstract methods/Interface
# Overriding

from abc import ABCMeta, abstractmethod

#Interface

class Shape(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width  = width
        self.height = height

        super(Rectangle, self).__init__()



rect = Rectangle(5,6)

print(rect.area())