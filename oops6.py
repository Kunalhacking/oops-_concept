# static method
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
        
    
    
# kunal=Employee()
# avinash=Employee()
ritesh=Employee(142,"RITESH","SDE-3")
rakhi=Employee.changeTwo("142-RAKHI-SDE3")

# kunal.salary=123
# kunal.name="KUNAL"
# kunal.role="SDE-1"

# avinash.salary=123
# avinash.name="AVINASH"
# avinash.role="SDE-2"


Employee.change(23)
# print(kunal.no_of_leaves)
# print(kunal.salary)
# print(avinash.salary)
# print(avinash.role)
# print(kunal.__dict__)
# print(avinash.__dict__)
# print(kunal.no_of_leaves)
# print(ritesh.__dict__)
print(rakhi.salary)
print(rakhi.__dict__)
rakhi.arella("karan")

