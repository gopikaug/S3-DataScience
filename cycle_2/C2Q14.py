print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:10/10/2023")
import numpy as np
"""matrix = np.array([[1, 2, 3],
                   [2, 4, 5],
                   [3, 5, 6]])"""
"""matrix = np.array([[0, 2, -3],
                  [-2, 0, 4],
                  [3, -4, 0]])"""
matrix= np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
transpose_matrix = np.transpose(matrix)
if np.array_equal(matrix, transpose_matrix):
    print("The matrix is symmetric.")
elif np.array_equal(matrix, -transpose_matrix):
    print("The matrix is skew symmetric.")
else:
    print("The matrix is neither symmetric nor skew symmetric.")