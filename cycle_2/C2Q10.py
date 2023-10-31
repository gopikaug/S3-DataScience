print("Name:Gopika Unnikrishnan\Roll No:22MCA030\nCourse Name:DATA SCIENCE LAB\Course Code:20MCA241\Date:10/10/2023")
import numpy as np
n = int(input("Enter the size of the square matrix: "))
random_matrix = np.random.randint(1, 10, (n, n))
try:
    inverse_matrix = np.linalg.inv(random_matrix)
except np.linalg.LinAlgError:
    inverse_matrix = None
    print("Matrix is not invertible.")
rank = np.linalg.matrix_rank(random_matrix)
determinant = np.linalg.det(random_matrix)
matrix_as_1d_array = random_matrix.flatten()
eigenvalues, eigenvectors = np.linalg.eig(random_matrix)
print("\nRandom Square Matrix:")
print(random_matrix)
if inverse_matrix is not None:
    print("\ni) Inverse Matrix:")
    print(inverse_matrix)
print("\nii) Rank of Matrix:", rank)
print("\niii) Determinant of Matrix:", determinant)
print("\niv) Matrix is 1D Array:")
print(matrix_as_1d_array)
print("\nv) Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
