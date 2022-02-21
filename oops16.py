#setters and property decorators
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname= lname
        # self.email= (f" email is : {self.fname}.{self.lname}@kunalteritory.com")# this can be use to
    
    def details(self):
        return(f" Employee first name  is {self.fname} and last name is {self.lname}")
    @property # property decorator # after if we use this as function it will through an error : str object is not collabe😂😂😂😂 
    def email(self):
        if self.fname==None or self.lname==None:
            print(f"Not set yet")
        else:
            return(f" email is : {self.fname}.{self.lname}@kunalteritory.com")
    
    @email.setter # it is used to set the new value of the attribute
    def email(self,string):
        print("Setting now..............")
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
        
    @email.deleter# it is used to delte attribute in property decorator
    def email(self):
        self. fname=None 
        self.lname=None
        
        
hindustan= Employee("Hindustani","Supporter")
kunal_kumar=Employee("kunal","kumar")
print(kunal_kumar.details())
print(hindustan.email)
hindustan.fname= "chinkandi"
print(hindustan.email)
del hindustan.email
hindustan.email
