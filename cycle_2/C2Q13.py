print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:16/10/2023")
import numpy as np
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
C = np.array([[9, 10],
              [11, 12]])
result = np.dot(np.dot(A, B), C)
print("Result of matrix multiplication:")
print(result)