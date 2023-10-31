print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:25/09/2023")
print("Equation : ax^2 + bx + c :")
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
d=b*b-4*a*c
if(d<0):
    print("The roots are imaginary")
else:
    r1=(-b+d)/2*a
    r2=(-b+d)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))