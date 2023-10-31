import numpy as np
try:
    print(
        "Name:Gopika Unnikrishnan\Roll No:22MCA030\Course Name:DATA SCIENCE LAB\Course Code:20MCA241\nDate:07/10/2023")
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
except ValueError:
    print("Please enter valid integer values for rows and columns.")
    exit()
complex_array = np.zeros((rows, columns), dtype=complex)
for i in range(rows):
    for j in range(columns):
        real_part = float(input(f"Enter the real part of element at position ({i}, {j}): "))
        imag_part = float(input(f"Enter the imaginary part of element at position ({i}, {j}): "))
        complex_array[i, j] = complex(real_part, imag_part)
print("\nComplex 2D Array:")
print(complex_array)
print(f"a. Number of rows: {rows}")
print(f"   Number of columns: {columns}")
dimensions = complex_array.ndim
print(f"b. Dimension of the array: {dimensions}")
reshaped_array = complex_array.reshape(3, 2)
print("\nReshaped 2D Array (3x2):")
print(reshaped_array)
