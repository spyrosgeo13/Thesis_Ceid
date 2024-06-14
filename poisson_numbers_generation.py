import numpy as np
import time 
from collections import Counter
import os 

def create_poisson_distribution_numbers_array():

    
    lamda = int(input("give the lamda"))
    size = int(input("give the size"))


    # creating the array s
    s = np.random.poisson(lamda,size)
    folder_path = "Distributions_unsorted/Poisson_distr"
    filename = f"Poisson_{size}.npy"


   
    full_path = os.path.join(folder_path, filename)
    
    # Save the created distribution in the specified folder
    np.save(full_path, s)
