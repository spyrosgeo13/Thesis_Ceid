import numpy as np
import os

def create_geometric_distribution_numbers_array():

    p= float(input("give the probability of success of individual trial: "))
    size = int(input("give the size of the array: "))

    s=np.random.geometric(p,size)
    #store the area in file  folder_path = "Distributions_unsorted/Poisson_distr"
    folder_path = "Distributions_unsorted/Geom_distr"
    filename = f"Geormetric_{size}.npy"


   
    full_path = os.path.join(folder_path, filename)
    
    # Save the created distribution in the specified folder
    np.save(full_path, s)
   