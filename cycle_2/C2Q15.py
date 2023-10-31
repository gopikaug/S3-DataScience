print("Name:Gopika Unnikrishnan\Roll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:10/10/2023")
import numpy as np
A = np.array([[2, 1,-2],
              [3,0,1],
              [1,1,-1]])
b = np.array([-3,5,2])
X = np.linalg.solve(A, b)
print("Solution for X:")
print(X)