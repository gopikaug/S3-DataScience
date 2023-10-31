print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:25/09/2023")
def gcd(x,y):
    if(x==0 or y==0):
        return 0
    if(x==y):
        return x
    if(x>y):
        return gcd(x-y,y)
    return gcd(x,y-x)
def coprime(x,y):
    if(gcd(x,y)==1):
        print("The Numbers",(x,y),"are Coprime")
    else:
        print("The Numbers", (x, y), "are not Coprime")
x=int(input("Enter the number(x):"))
y=int(input("Enter the number(y):"))
coprime(x,y)


