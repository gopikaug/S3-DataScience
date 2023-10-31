print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:25/09/2023")
x=int(input("Enter lower digit:"))
y=int(input("Enter upper digit:"))
print("lower=",x)
print("upper",y)
print("The prime numbers in between the range ",x,"to",y)
for n in range(x, y+1):
    if(n > 1):
        for i in range(2,n):
            if(n % i) == 0:
                print(n)
                break