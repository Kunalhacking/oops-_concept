# MULTILEVEL INHERITANCE
class Electronic_device:
    Tablet= 22
class Pocket_gadget(Electronic_device):
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