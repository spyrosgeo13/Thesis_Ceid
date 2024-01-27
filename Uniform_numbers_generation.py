
import numpy as np
import os

def create_uniform_distribution_numbers_array():

    size = int(input("give the size"))
    low= int(input("give the Lower boundary of the output interval"))
    high = int(input("give the Upper boundary of the otput interval"))

    s =  np.random.random_integers(low, high , size)
    # Specify the folder path where you want to save the file
    folder_path = "Distributions_unsorted"  # Replace with the actual folder path
    
    # Create a filename based on the size
    filename = f"Uniform_{size}.npy"
    
    # Join the folder path and filename
    full_path = os.path.join(folder_path, filename)
    
    # Save the created distribution in the specified folder
    np.save(full_path, s)
    #s = np.default_rng().uniform(low,high,size)
    s =  np.random.random_integers(low, high , size)
    #save the created distribution
    np.save("Uniform.npy",s)

    

