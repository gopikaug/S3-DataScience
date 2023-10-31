print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:10/10/2023")
import numpy as np
n = int(input("Enter the number of elements in the 1D array: "))
one_d_array = np.empty(n, dtype=int)
for i in range(n):
    one_d_array[i] = int(input(f"Enter element {i + 1}: "))
element_to_insert = int(input("Enter the element to insert: "))
index_to_insert = int(input("Enter the index at which to insert: "))
result_1d = np.insert(one_d_array, index_to_insert, element_to_insert)
print("1D Array after insertion:")
print(result_1d)
rows = int(input("Enter the number of rows in the 2D array: "))
columns = int(input("Enter the number of columns in the 2D array: "))
two_d_array = np.empty((rows, columns), dtype=int)
for i in range(rows):
    for j in range(columns):
        two_d_array[i, j] = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
element_to_insert = int(input("Enter the element to insert:"))
row_to_insert = int(input("Enter the row index at which to insert: "))
column_to_insert = int(input("Enter the column index at which to insert: "))
result_2d = np.insert(two_d_array, (row_to_insert, column_to_insert), element_to_insert)
print("2D Array after insertion:")
print(result_2d)
