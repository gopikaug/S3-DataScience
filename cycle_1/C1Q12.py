vowels='aeiou'
print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:03/10/2023")
a=input("Enter the string:")
a=a.casefold()
count={}.fromkeys(vowels,0)
for char in a:
    if char in count:
            count[char] +=1
print(count)