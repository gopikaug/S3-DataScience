print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:10/10/2023")
import numpy as np
A = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]])
B = np.array([[2, 1, 0],
              [0, 2, 0],
              [1, 0, 1]])
submatrix = A[:3, :3]
print('Extracted submatrix:\n', submatrix)
result = np.dot(submatrix, B)
print('Result: \n', result)
A[:3, :3] = result
print("Matrix A after replacing the submatrix with the result:")
print(A)