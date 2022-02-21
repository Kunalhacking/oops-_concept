# \ LAYER OF ABSTRACTION : IF WE WANT TO ACHIEVE ABSTRACTION WE NEED TO USE ENCAPSULATION :this is use to hide the implimentation
class Employee:
    no_of_leaves=10
    def __init__(self,salary,name,role):# we use constructor  to add a specific value of the object
        self.salary = salary
        self.name = name
        self.role = role
    
    @classmethod# we use classmethods to  change the value of class instance
    def change(cls,leave):
        cls.no_of_leaves=leave
    @classmethod   
    def changeTwo(cls,string):
        str= string.split("-")
        return cls(str[0],str[1],str[2])
    @staticmethod
    def arella(string):
        print(f"this method is only for"+" "+string)
ritesh=Employee(142,"RITESH","SDE-3")
rakhi=Employee.changeTwo("142-RAKHI-SDE3")
Employee.change(23)
print(rakhi.salary)
print(rakhi.__dict__)
rakhi.arella("karan")

 