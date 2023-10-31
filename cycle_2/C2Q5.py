print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:07/10/2023")
import numpy as np
even_numbers = np.arange(2, 32, 2)
print("First 15 even numbers as elements:")
print(even_numbers)
elements_from_2_to_8_step_2 = even_numbers[2:9:2]

print("a. Elements from index 2 to 8 with step 2:", elements_from_2_to_8_step_2)
last_3_elements = even_numbers[-3:]
print("b. Last 3 elements of the array using negative index:", last_3_elements)
alternate_elements = even_numbers[::2]
print("c. Alternate elements of the array:", alternate_elements)
last_3_alternate_elements = even_numbers[-1::-2][:3]
print("d. Last 3 alternate elements of the array:", last_3_alternate_elements)
