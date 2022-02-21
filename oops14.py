# abstract base class 
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0
class rectangle(shape):
    def __init__(self):
        self.length= 12
        self.breadth=6
    def printArea(self):
        return self.length*self.breadth
class square(rectangle):
    def printArea(self):
        return self.length*self.breadth
c=square()
a=rectangle()
print(a.printArea())
print(c.printArea())
        
        
        
