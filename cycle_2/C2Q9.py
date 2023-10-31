print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:10/10/2023")
import numpy as np
arr_1d = np.array([1, 2, 3])
diagonal_matrix = np.diag(arr_1d)
print(diagonal_matrix)
square_matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
diagonal_1d = np.diag(square_matrix)
print(diagonal_1d)
rectangular_matrix = np.array([[1, 2, 3],
                               [4, 5, 6]])
diagonal_1d = np.diag(rectangular_matrix)
print(diagonal_1d)