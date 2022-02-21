# multiple inheritance

class Employee:
    v=12
    no_of_leaves=22
    def __init__(self,name,Salary,role):
        self.name = name
        self.Salary = Salary
        self.role = role
    def printdetails(self):
        print(f"the name is {self.name}, the salary is {self.Salary}, the role is {self.role}")
    @classmethod
    def change(cls,leave):
        cls.no_of_leaves = leave
Kunal=Employee("kunal",123,"SDE-4")
aman=Employee("aman",999,"SDE-4")

print(aman.__dict__)
Kunal.printdetails()
Kunal.change(23)
print(Kunal.no_of_leaves)

class programmer(Employee):
    v=13
    no_of_prog=100
    
    def __init__(self,name,Salary,role):
        self.name = name
        self.Salary = Salary
        self.role = role
    def printdetails(self):
        print(f"the name is {self.name}, the salary is {self.Salary}, the role is {self.role}")
karan =programmer("karan",999,"programmer")
class Player:
    v=14
    no_of_games=10
    def __init__(self,name,games):
        self.name=name
        self.games= games
    def printGames(self):
        print(f"the name is {self.name} and the game is {self.games}")
    @classmethod
    def getChange(cls,no_game):
         cls.no_of_games =no_game 
class Coolprogrammer(Employee,Player):
    pass
shubham=Player("shubham","[cricket, football]")
print(shubham.games)
ritesh=Coolprogrammer("ritesh",8999,"cool")
print(ritesh.__dict__)
ritesh.printdetails()
print(ritesh.no_of_games)
ritesh.getChange(100)
print(ritesh.no_of_games)
print(ritesh.v)




        