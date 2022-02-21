class Employee:
    no_of_leaves= 12 
    def __init__(self,aname,asalary,arole):#constructor
        self.name=aname
        self.salary= asalary
        self.role=arole
        
    def print_details(self):
            return f"Name is {self.name}, Salary is {self.salary}, role is {self.role}"
    
kunal=Employee("kunal",12000,"instructor")
amit=Employee()

kunal.name="kunal"
kunal.role="instructor"
kunal.salary=100000

amit.name= "amit"
amit.role="software Engineer"
amit.salary=120000

print(kunal.print_details())
print(amit.print_details())
print(kunal.salary)