import numpy as np
import time 




def create_poisson_distribution_numbers_array():

    
    lamda = int(input("give the lamda"))
    size = int(input("give the size"))


    # creating the array s
    s = np.random.default_rng().poisson(lamda,size)
    
    #store the  created array in a file 
    np.save("poisson.npy", s)