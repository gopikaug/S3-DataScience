print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:07/10/2023")
import numpy as np
try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
except ValueError:
    print("Please enter valid integer values for rows and columns.")
    exit()
print("\nEnter elements for Matrix 1:")
matrix1 = np.zeros((rows, columns), dtype=int)
for i in range(rows):
    for j in range(columns):
        matrix1[i, j] = int(input(f"Enter element at position ({i+1}, {j+1}): "))
print("\nEnter elements for Matrix 2:")
matrix2 = np.zeros((rows, columns), dtype=int)
for i in range(rows):
    for j in range(columns):
        matrix2[i, j] = int(input(f"Enter element at position ({i+1}, {j+1}): "))
result_addition = matrix1 + matrix2
result_subtraction = matrix1 - matrix2
result_elementwise_multiplication = matrix1 * matrix2
result_elementwise_division = matrix1 / matrix2
result_matrix_multiplication = np.dot(matrix1, matrix2)
matrix1_transpose = np.transpose(matrix1)
diagonal_sum = np.trace(matrix1)
print("\nMatrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\na. Addition of the two matrices:")
print(result_addition)
print("\nb. Subtraction of the two matrices:")
print(result_subtraction)
print("\nc. Element-wise multiplication of the two matrices:")
print(result_elementwise_multiplication)
print("\nd. Element-wise division of the two matrices:")
print(result_elementwise_division)
print("\ne. Matrix multiplication:")
print(result_matrix_multiplication)
print("\nf. Transpose of Matrix 1:")
print(matrix1_transpose)
print("\ng. Sum of diagonal elements of Matrix 1:")
print(diagonal_sum)
