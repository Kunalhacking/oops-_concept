#generators
def generate(n):
    if n==0: return 0
    elif n==1: return  1
    else: yield generate(n-1)+generate(n-2)
def fac(n): 
    if n==1 :return 1
    else: yield n*fac(n-1)
print(f" the generator of fabonacci is {generate(5)}.\n the generator of factorial is {fac(5)}.")

    
    