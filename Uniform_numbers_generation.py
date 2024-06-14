import numpy as np
import os

def create_uniform_distribution_numbers_array():

    size = int(input("Give the size: "))
    low = float(input("Give the lower boundary of the output interval: "))
    high = float(input("Give the upper boundary of the output interval: "))

    s = np.random.uniform(low, high, size)
    
    # Specify the folder path where you want to save the file
    folder_path = "Distributions_unsorted/Uniform_distr"  # Replace with the actual folder path
    
    # Create a filename based on the size
    filename = f"Uniform_{size}.npy"
    
    # Join the folder path and filename
    full_path = os.path.join(folder_path, filename)
    
    # Save the created distribution in the specified folder
    np.save(full_path, s)
