
import numpy as np


def create_uniform_distribution_numbers_array():

    size = int(input("give the size"))
    low= int(input("give the Lower boundary of the output interval"))
    high = int(input("give the Upper boundary of the otput interval"))

    
    #s = np.default_rng().uniform(low,high,size)
    s =  np.random.uniform(low, high , size)
    
    for i in range(0, len(s)):
        print(s[i])

    

