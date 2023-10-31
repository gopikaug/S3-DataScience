print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:17/10/2023")
import pandas as pd
iris_data=pd.read_csv('iris.csv')
print("\ni) Shape of the dataset:")
print(iris_data.shape)
print("\nii) First 5 and last five rows of data set(head and tail):")
print(iris_data.head())
print(iris_data.tail())
dataset_size = iris_data.shape[0]
print("\niii)Size of the dataset:", dataset_size)
sample_counts = iris_data['variety'].value_counts()
print("\niv) Number of samples available for each variety:")
print(sample_counts)
dataset_description = iris_data.describe()
print("\nv) Description of the dataset:")
print(dataset_description)

