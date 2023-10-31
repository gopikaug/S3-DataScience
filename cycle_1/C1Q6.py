print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:25/09/2023")
n = int(input("Enter the number="))
sum=0
for i in range(1,n):
    if(n % i == 0):
        sum=sum+i
if(sum==n):
    print("The Number",n,"is a Perfect Number")
else:
    print("The Number", n, "is not Perfect Number")

