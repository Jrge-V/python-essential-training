# Using Abstract Base Classes to implement interfaces

# You can think of an interface as a promise or a 'contract' to provide...
# ... some kind of behavior or capability

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f'{{"Circle": {str(self.calcArea())}}}'


c = Circle(10)
print(c.calcArea())
print(c.toJSON())