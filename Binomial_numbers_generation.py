import numpy as np
import os 

def  create_binomial_distribution_numbers_array(): 
    
    
    
    n = int(input("give trials number"))
    p = float(input("set probability of success"))
    size = int(input("give output size"))


    s = np.random.binomial(n,p,size)

    #save the binomial distribution 
    folder_path = "Distributions_unsorted/Binom_distr"
    filename = f"Binomial_{size}.npy"


   
    full_path = os.path.join(folder_path, filename)
    
    # Save the created distribution in the specified folder
    np.save(full_path, s)
    