class Student:
    no_of_leaves=120#class variable
    def __init__(self, name,salary,role):#instance variable
        self.salary= salary
        self.name=name
        self.role =role
        
@classmethod# can be acessed by  any object of the class
def change_no_of_leaves(cls,leaves):
        cls.no_of_leaves= leaves
    
    
kunal= Student("KUNAL",12470000,"SDE-2")
    
mukesh= Student("MUKESH",1229999,"SDE-2")
aman=Student("AMAN",123456,"SDE-3")

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








# def dec(function):
#     def exec():
#         print("Executing")
#         function()
#         print("executing now")
#     return exec

# @dec
# def who_is_kunal():
#     print("kunal")
    
    
# who_is_kunal()