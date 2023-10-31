print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:10/10/2023")
import numpy as np
X = np.array([[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10]])
cubed_elements_1 = X ** 3
cubed_elements_2 = np.power(X, 3)
cubed_elements_3 = np.multiply(X, X) * X
cubed_elements_4 = X * X * X
print("i) Cube of each element of the matrix (Method 1):\n", cubed_elements_1)
print("\nCube of each element of the matrix (Method 2):\n", cubed_elements_2)
print("\nCube of each element of the matrix (Method 3):\n", cubed_elements_3)
print("\nCube of each element of the matrix (Method 4):\n", cubed_elements_4)
identity_matrix = np.identity(X.shape[0])
print("\nii) Identity matrix of the given square matrix:\n", identity_matrix)
squared_elements = np.power(X, 2)
cubed_elements = np.power(X, 3)
print("\niii) Squared elements of the matrix:\n", squared_elements)
print("\nCubed elements of the matrix:\n", cubed_elements)
Y = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
result = X**2 + 2*Y
print("Result of the operation X^2 + 2Y:\n", result)