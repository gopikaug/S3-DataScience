import numpy as np
try:
    print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:07/10/2023")
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
except ValueError:
    print("Please enter valid integer values for rows and columns.")
    exit()
uninitialized_array = np.empty((rows, columns))
print("Uninitialized Array:")
ones_array = np.ones((rows, columns))
print(uninitialized_array)
print("Array with All Elements as 1:")
print(ones_array)
zeros_array = np.zeros((rows, columns))
print("Array with All Elements as 0:")
print(zeros_array)
