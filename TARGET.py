# ###########################WEEKLY TARGET######################################
# # I HAVE TO DO PROBLEMS ON  LOOP
# # I HAVE TO DO REVISION OF CLASS METHODS 
# # I HAVE TO DO REVISION OF ENUMRETS METHOD
# # I HAVE TO DO REVISION OF DECORATORS METHOD
# # I HAVE TO REVISION OF FUNCTION 
# # I HAVE TO DO REVISON OF DICT FUNCTIONS
# # I HAVE TO DO REVISON OF OPERATORS(AND,OR,XOR, XNOR)
# # BOOL VARIABLES (PRACTICE)
# # FILE SYSTEM SYNTAX FUNCTIONS
# ###############################################################################
# # n = int(input("enter the number of  rows :"))
# # bool= int(input("type 1 or 0 :"))
# # if bool== 1:
# #     for  i in range(n):
# #         for j in range(i+1):
# #             print("*",end="")
# #         print()
# # elif bool== 0:
    
# #     for i  in range(n):
# #         for j in range(i,n):
# #             print("*", end="")
# #         print()
# # else:
# #     print("invalid input")
                
                
                
                





# # class Employee:
# #     leaves=122
# #     def __init__(self, name, salary,role):
# #         self.name=name
# #         self.salary=salary
# #         self.role=role
# #     @classmethod 
# #     def change_leaves(cls,leave):# this function can only  be call by class object
# #         cls.leaves=leave
# #     @classmethod
# #     def details(cls,string):
# #         string=string.split("-")
# #         return cls(string[0],string[1],string[2])
        
# # emp_1=Employee("amit","134","sde-1")
# # emp_2=Employee("kunal",1234,"sde-2")
# # emp_3=Employee.details("raman-124-sde4")
# # print(emp_1.name,emp_1.salary,emp_1.role)
# # print(emp_2.name,emp_2.salary,emp_2.role)
# # emp_1.change_leaves(34)
# # print(emp_1.leaves)
# # print(emp_2.leaves)
# # print(emp_3.salary)
# # print(emp_3.__dict__)





# # n=input("enter the string you want to print\n")

# # for i in range(len(n)):
# #     for j in range(i+1):
# #         print(n[j],end="")
# #     print()
    
    
# # list=[1,2,3,4,5,6,7,8,9,10]
# # for index,item in enumerate(list):
# #     print(index,item)

# # def str_split(string):
# #     str=string.split("_")
# #     return str[0],str[1],str[2],str[3]
# # print(str_split("kunal_is_a_good_boy")

# # i=0
# # while(i<=45):
# #     print(i,end=" ")
# #     i =i+1

# # n=18
# # print("total no of guess given in this game is 9")
# # no_of_guess=1
# # while(no_of_guess<=9):
# #     inp=int(input("enter the first guess for this game"))
# #     if inp<n:
# #         print("increase")
# #     elif inp>n:
# #         print("decrease")
# #     else:
# #         print("you won")
# #         break
# #     print("no of guess left is",9-no_of_guess)
# #     no_of_guess+=1
# #     if no_of_guess>9:
# #         print("you lost")

# # while(True):
# #     n=int(input("enter the number"))
# #     if n<=100:
# #         print("congratulation")
# #         break
# #     print("try again")
# #     continue 
# # n= int(input("enter the number"))
# # for i in range(n):
# #     if n<=100:
# #         print("congratulation")
# #         break
# #     else:
# #         print("try again") 
         
# #function to break a atring 
# # def split(string):

# #     str=string.split("-")
# #     return str[0],str[1],str[2],str[3],str[4]
# # string="he-is-a-good-man"
# # print(split(string))



# #patterns#
# # n=int(input("enter the number of rows "))
# # for i in range(n):
# #     for j in range(i+1):
# #         print("^",end=" ")
# #     print()
# # def func(num):
# #     if num%2==0:
# #         return f"the number is even"
# #     else:
# #         return f"the number is odd"
# # num=int(input("enter the number"))
# # print(func(num))
    
# # list=[1,2,3,4,5,6,7,8]
# # for i in list:
# #     if i%2!=0:
# #         print(f"{i} is a prime number")
# #     else:
# #         print(f"{i} is not a prime no")



# # def sum(n):
# #     if n==0:
# #         return 1
# #     return n*n*n
# # n= int(input("enter the maimum range"))
# # for i in range(1,n+1):
# #     print(sum(i))
# # basic maths 
# # number system 
# # number theory 
# # def countCubeSumPairs(n):

#     # Counter counting the number of pairs of (a,b).
# # def countCubeSumPairs(n):

# #     # Counter counting the number of pairs of (a,b).
# #     count = 0
# #     # Iterating through all the possible values of 'a'.
# #     for a in range(1, n + 1):
# #         # Iterating through all the possible values of 'b' 
# #         for b in range(n + 1):
# #             # Calculating value of 'a'^3 and 'b'^3.
# #             a3 =  a * a * a
# #             b3 =  b * b * b
# #             '''
# #                 If 'a'^3 + 'b'^3 is equals to 
# #                 n then incrementing the counter.
# # 			'''
# #             if a3 + b3 == n:
# #                 count += 1
        

# #     # Returning the count of required (a,b) pairs for given 'n'.
# #     return count

# # n= int(input("enter"))

# # for i in range(2,int(n/2)):
# #     if n%i==0:
# #         print(f"{n} :is not prime ")
# #         break
# #     else:
# #         print(f"{n} :prime")
    
    
# # def isPrime(num):
# #     if num==1:
# #         return False
# #     for i in range(2,int(num/2)+1):
# #         if num%i==0: 
# #             return False
# #     return True
# # for i in range(1,21):
# #     if isPrime(i):
# #         print(i)
# # import math
# # def isPrime(num):
# #     if num==1:
# #         return False
# #     for i in range(2,int(math.sqrt(num)+1)):
# #         if num%i==0:
# #             return False
# #     return True
# # print(isPrime(573)) 
                                               
# # def DiamondPattern(n):
# #     for i in range(n-1):
# #         for j in range(i,n):
# #             print(" ",end="")
# #         for j in range(i+1):
# #             print("*",end=" ")
# #         print()
# #     for i in range(n):
# #         for j in range(i+1):
# #             print(" ",end="")
# #         for j in range(i,n):
# #             print("*",end=" ")
# #         print() 
# # n=5  
# # print(DiamondPattern(5))

# # def string(string):
# #     for i in range(len(string)):
# #         for j in range(i+1):
# #             print(string[j],end="")
# #         print()
# # print(string("Kunal")
# #concpet of prime number 
# # import math
# # def isPrime(n):
# #     if n==1:
# #         return False
# #     for i in range(2,int(math.sqrt(n)+1)):
# #         if n%i==0:
# #             return False
# #     return True
# # print(isPrime(24))


# # def function(n):
# #     return
# # def function(n):
# #     if n==0:
# #         return True
# #     sum=0 
# #     for i in range(0,n):
# #         if sum==n:
# #             return True
# #     return False   
# # for i in range(0,n):
# # print(function(6))


# from asyncore import write


# class Employee:
#     no_of_leaves=10
#     def __init__(self,salary,name,role):# we use constructor  to add a specific value of the object
#         self.salary = salary
#         self.name = name
#         self.role = role
    
#     @classmethod# we use classmethods to  change the value of class instance
#     def change(cls,leave):
#         cls.no_of_leaves=leave
#     @classmethod   
#     def changeTwo(cls,string):
#         str= string.split("-")
#         return cls(str[0],str[1],str[2])
#     @staticmethod
#     def arella(string):
#         print(f"this method is only for"+" "+string)
        
    
    
# # kunal=Employee()
# # avinash=Employee()
# ritesh=Employee(142,"RITESH","SDE-3")
# rakhi=Employee.changeTwo("142-RAKHI-SDE3")

# # kunal.salary=123
# # kunal.name="KUNAL"
# # kunal.role="SDE-1"

# # avinash.salary=123
# # avinash.name="AVINASH"
# # avinash.role="SDE-2"


# Employee.change(23)
# # print(kunal.no_of_leaves)
# # print(kunal.salary)
# # print(avinash.salary)
# # print(avinash.role)
# # print(kunal.__dict__)
# # print(avinash.__dict__)
# # print(kunal.no_of_leaves)
# # print(ritesh.__dict__)
# print(rakhi.salary)
# print(rakhi.__dict__)





# def sqrtN(N):
# 	#  Take 'ans' variable to store the square root of given number 'N'
# 	ans = 1
	
# 	# Run loop while square of 'ans' is less than equal to 'N'
# 	while(ans <= (N // ans)):
		
# 		# Increament 'ans' by 1
# 		ans += 1
		
# 	# Return 'ans'-1
# 	return (ans - 1)


# with open("kunal.txt", "r") as f:
#     print(f.read(134))

# def isPrime(n):
#     if n==1:
#         return False
#     for i in range(2,int(n/2)+1):
#         if n%i==0:
#             return False
#     return True
# print(isPrime(19))

# class Emp:
#     no_of_leaves=123
#     def __init__(self, name,salary):
#         self.name=name
#         self.salary=salary
#     def printdetails(self):
#         print(f"the salary is {self.salary} , the name is {self.name}")
# kunal=Emp("kunal",999)

# class b(Emp):
#     holiday=10
#     # def __init__(self,name, salary):
#     #     self.name=name
#     #     self.salary=salary
#     def print(self):
#         return (f" the name  is {self.name} and salary is {self.salary}")
#     @classmethod
#     def split(cls,string):
#         str= string.split("-")
#         return cls(str[0],str[1])
# karan=b("karan",8999)
# amit=b.split("amit-100000")
# class games:
#     games=12
#     def __init__(self,name, game):
#         self.name=name
#         self.game= game
#     def printGames(self):
#             return (f"the name is {self.name} and the game is {self.game}")
# karan=games("karan","hockey")

# class coolprog(Emp,games):
#     pass
# shubham=games("shubham","hockey")  
# karan= Emp("Karna","3400000")

# print(shubham.printGames())   
# print(karan.printdetails()) 


# multilevel inheritancede

# class a:
#     guitar=12
#     _var=12#(protected)
#     __g=13
# class b(a):
#     iphones =100  
#     def phones(self):
#         return (f"no of phones {self.iphones}")
# class c(b):
#     def __init__(self, name,salary):
#         self.name= name
#         self.salary=salary
#     def printdetails(self):
#         return (f" name is {self.name} and salary is {self.salary}")
# shubha=c("shubha",123)
# class d(c):
#     no_of_bands= 12
#     @classmethod
#     def split(cls,string):
#         str=string.split("-")
#         return cls(str[0],str[1])
# karan=d.split("karan-19000")
# print(karan.guitar)
# print(shubha.phones())
# print(shubha.guitar)
# print(b._var)
# print(a._a__g)# acess the private only acess by reprensentative class
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname= lname
#         # self.email= (f" email is : {self.fname}.{self.lname}@kunalteritory.com")# this can be use to
    
#     def details(self):
#         return(f" Employee first name  is {self.fname} and last name is {self.lname}")
#     @property # property decorator # after if we use this as function it will through an error : str object is not collabe😂😂😂😂 
#     def email(self):
#         if self.fname==None or self.lname==None:
#             print(f"Not set yet")
#         else:
#             return(f" email is : {self.fname}.{self.lname}@kunalteritory.com")
    
#     @email.setter # it is used to set the new value of the attribute
#     def email(self,string):
#         print("Setting now..............")
#         name=string.split("@")[0]
#         self.fname=name.split(".")[0]
#         self.lname=name.split(".")[1]
        
#     @email.deleter# it is used to delte attribute in property decorator
#     def email(self):
#         self. fname=None 
#         self.lname=None
# hindustan= Employee("Hindustani","Supporter")
# kunal_kumar=Employee("kunal","kumar")
# print(kunal_kumar.email)
# sum of n natural no"s

# n= int(input("enter the number"))
# i=0
# sum=0
# while(i<=n):
#     sum= sum+i
#     i= i+1
# print(sum)

# sum of n even numbers

# n=int(input("enter the number"))
# i=0
# sum=0
# while(i<=n):
#     print
#     sum=sum+i
#     i+=2
# print(f"the sum of even numbers are : {sum}")

# n=int(input("enter the number"))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i+=2
# print(f"the sum of odd numbers are : {sum}")

# 0,1,2,3,4,5,6,7,8,9 even
# 1,3,5,7,9 odd
# reverse numbers 
# n=int(input("enter the number"))
# rev=0
# if n<10:
#     print(f" invalid number please enter 2 digit no atleast or greater")
# else:
#     while(n>0):
#         dig= n%10
#         rev=rev*10+dig
#         n=n//10
# print(f"The reverse of the number is:{rev}")

# def arm(n):
#     if n<=10: return n*n*n
#     else:return (n%10)*(n%10)*(n%10)+arm(n//10)
# num= int(input("Enter the number "))
# if num==arm(num):
#     print(f"The number is armstrong :{num}")
# else:
#     print(f" Not an armstrong number:{num}")
# def list(n):  
#     list=[]
#     for i in range(n):
#         if i%2==0:
#             list.append(i)
#     return list
# print(list(12))
# import math
# def prime(n):
#     # lst=[]
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:return False
#     return True
# print(prime(10)
# n=int(input("enter the number"))
# for i in range(2,n//2+1):
#     if n%i==0:
#         print(f"Not prime:{n}")
#         break
#     else:
#         print(f"prime")
#         break



# char="kunal": add total no of alphabetic characters

# def split(string):
#     str=s5
# guess the number by the user
# n=18
# print(f"welcome to the guess game")
# no_of_guess=1
# inp=int(input("Enter the guess"))
# while(no_of_guess<=8):
#     if inp<n:
#         print(f"please increase")
#     elif inp>n:
#         print(f"please decrease")
#     else:
#         print(f"you won")
#         print("total no of guess is ",no_of_guess)
#         break 
#     print("no of guess he took",8-no_of_guess)
#     no_of_guess+=1
    
# if no_of_guess>8:
#     print(f"you lost")

# dict={1:"kunal",2:"aman",3:"vishal"}
# print(dict)         
# print(dict.keys())
# print(dict.values())
# d1= dict.copy()# to copy but the base dict will be immutable
# d1[4]="mitra"#// to add
# print(d1)
# d1.update({5:"kebab"})# this is also used to update
# print(d1)

# print(dict)

# ls=["bhindi", "chopsticks","chop_chop"]
# for index,item in enumerate(ls):
#     print(index,item,end="|")


# list=[2,4,5,8]
# ls=[]
# for i in list:
#     if i%2==0:
#         ls.append(i)
# print(ls)

# numbers=[1,2,3,4,5,6,7,8,9]
# # count no of even and odd numbers in the list

# count_odd=0
# count_evens=0
# for num in numbers:
#     if num%2==0:
#         count_evens+=1
#     else:
#         count_odd+=1
# print(count_odd)
# print(count_evens)


 
# furniture_count=["table[i]","chair","desk","lamp","couch"]
# i=0
# while(i<len(furniture_count)):
#     print(f"you will not able to find:{furniture_count[i].upper()}:in this mart")
#     i+=1
# count no of evens and odds:

# list=[1,2,3,4,5,6,7,8,9,10,11,12]
# i=0
# count_even =0
# count_odd=0
# while(i<len(list)):
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
#     i+=1
# print(f"no of evn in list:{count_even}")
# print(f"no of odd in list:{count_odd}")

# list=[[1,2],[3,4],[5,6],7,8]
# for ele in list:
#     ele.sort(reverse=True)
# print(f"the orignal list is:{list}+{str(list)}")
# def stri(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
# print(stri("kunal"))
# def reverse(s):
#     if len(s)==0:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
# print(reverse("kunal"))