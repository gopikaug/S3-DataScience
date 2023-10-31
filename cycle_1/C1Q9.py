print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:26/09/2023")
list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    num1 = int(input())
    list1.append(num1)
print("The List-1:",list1)
list2 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    num2 = int(input())
    list2.append(num2)
print( "The List-2:",list2)
sum_list = []
for i in range(0, len(list1)):
    sum_list.append(list1[i] + list2[i])
print("Resultant list is :" + str(sum_list))