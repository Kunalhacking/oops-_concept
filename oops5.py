class Student:
    no_of_leaves=120#class variable
    def __init__(self, name,salary,role):#instance variable
        self.salary= salary
        self.name=name
        self.role =role
@classmethod
def from_dash(cls,string):
    v= string.split("-")
    return cls(v[0],v[1],v[2])
        
        
kunal= Student("KUNAL",12470000,"SDE-2")   
mukesh= Student("MUKESH",1229999,"SDE-2")
aman=Student("AMAN",123456,"SDE-3")
amit=Student.from_dash("karan-12345678-Sde-4")

print(kunal.salary)
print(kunal.role)
print(kunal.name)


print(mukesh.salary)
print(mukesh.role)
print(mukesh.name)

Student.change_no_of_leaves(45)
print(kunal.no_of_leaves)
print(mukesh.no_of_leaves)
print(kunal.salary)
print(aman.role)
print(amit.role)
