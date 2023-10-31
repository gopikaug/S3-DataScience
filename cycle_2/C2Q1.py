import numpy as np
try:
    dim1 = int(input("Enter the size of the first dimension: "))
    dim2 = int(input("Enter the size of the second dimension: "))
    dim3 = int(input("Enter the size of the third dimension: "))
except ValueError:
    print("Please enter valid integer values for dimensions.")
    exit()
array_3d = np.random.rand(dim1, dim2, dim3).astype(float)
print("Generated 3D array:")
print("The Array:",array_3d)
