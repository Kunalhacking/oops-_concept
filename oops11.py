# public ,protected ,classifiers

# oops  prespective
#Public: paste outside the home

#Private:paste in room #this can be acessed by using _x(single underscore)
#Protected:paste in house #this can be acessed by using __x(double underscore)



class Electronic_device:
    Tablet= 22
    _v= 28# protected member
class Pocket_gadget(Electronic_device):
    __g=12# private member
    Iphones= 34
    Android_phone=11
    def printPhones(self):
        return(f"no of iphones are {self.Iphones} and no of Android devices are {self.Android_phone}")
class Phone(Pocket_gadget):
    def __init__(self,name,range):
        self.name = name
        self.range = range
Apple = Phone("iphone","150000")
oppo = Phone("oppo","15000")

print(oppo.Android_phone)
print(Apple.Iphones)
print(Apple.Tablet)
print(oppo.Tablet)
print(Apple.__dict__)
print(Apple.printPhones())
print(Apple.name)
print(oppo.range)
print(Apple._v)# to acess protected member # used for child class
print(Apple._Pocket_gadget__g)# to acess private member # this can be acessed by base class only 
