print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241")
n = int(input("Number of terms:"))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Please enter a Postive Integer")
elif n==1:
    print("Fibonacci series upto",n,":")
    print(n1)
else:
    print("Fibonacci Series:")
    while count < n:
        print(n1)
        nth=n1+n2
        n1 = n2
        n2 = nth
        count += 1
