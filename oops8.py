
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
class programmer(Employee):#SINGLE INHERITENCE CONCEPT
    holiday=22
    def __init__(self,salary,name,role,lang):
        self.salary = salary
        self.name = name
        self.role = role
        self.lang=lang
        
    def printdetails(self ):
        return (f"salary is{self.salary} and name is{self.name} and role is{self.role} and language is{self.lang}")
    @classmethod
    def change(cls,holiday_one):
        cls.holiday=holiday_one
    
shubham=programmer(142,"SHUBHAM","SDE-3",["cpp","pyhton"])
amit=programmer(142,"amit","SDE-3",["cpp","pyhton"])
        
ritesh=Employee(142,"RITESH","SDE-3")
rakhi=Employee.changeTwo("142-RAKHI-SDE3")
Employee.change(23)
print(rakhi.salary)
print(rakhi.__dict__)
rakhi.arella("karan")
print(shubham.printdetails())
print(shubham.lang)
print(amit.holiday)
programmer.change(34)
print(shubham.holiday)
print(Employee.no_of_leaves)




 