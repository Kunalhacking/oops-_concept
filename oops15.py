# mapping operator and dunder method
# https://docs.python.org/3/library/operator.html#:~:text=Mapping%20Operators%20to%20Functions%20%C2%B6%20%20%20,truediv%20%28a%2C%20b%29%20%2031%20more%20rows%20
# repr or str method

class employee:
    no_of_leaves=12 
    def __init__(self, name, salary ,role):
        self.name = name
        self.salary = salary
        self.role = role
    def print(self):
        print(f" the name is {self.name}, salary is {self.salary}, role is {self.role}")
    @classmethod
    def change(cls,leaves):
        cls.no_of_leaves= leaves
    def __add__(self,other):# dunder method( special metheod to perform special operations in the object)
        # it help us to do operator overloading
        return self.salary + other.salary
    def __truediv__(self,other):return self.salary / other.salary
    def __mod__(self,other):return self.salary % other.salary
    def __mul__(self,other):return self.salary * other.salary
    def __repr__(self):return (f"employee({self.name},{self.salary},{self.role})")
    def __str__(self):return(f" the name is {self.name}, salary is {self.salary}, role is {self.role}")
        
emp1=employee("kunal",123,"sde-1")
emp2=employee("shikari",12,"cleaner")
print(emp1.no_of_leaves)
employee.change(130)
print(emp1.no_of_leaves)
print(emp1+emp2)
print(emp1/emp2)
print(emp1%emp2)
print(emp1*emp2)
# repr method 
print(repr(emp1))
# str method
print(str(emp1))

