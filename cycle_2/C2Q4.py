print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:07/10/2023")
import numpy as np
arr = np.arange(10)
print("One-Dimensional Array:")
print(arr)
try:
    start_index = int(input("Enter the starting index: "))
    end_index = int(input("Enter the ending index: "))
except ValueError:
    print("Please enter valid integer values for indices.")
    exit()
if start_index >= 0 and end_index <= 9:
    a_slice = arr[:4]  # First 4 elements
    b_slice = arr[4:]  # Last 6 elements
    c_slice = arr[start_index:end_index + 1]

    print("\na. First 4 elements:")
    print(a_slice)

    print("\nb. Last 6 elements:")
    print(b_slice)

    print("\nc. Elements from index {} to {}: ".format(start_index, end_index))
    print(c_slice)
else:
    print("Invalid indices. The indices should be between 0 and 9.")
