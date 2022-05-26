import numpy as np

def  create_binomial_distribution_numbers_array(): 
    
    
    
    n = int(input("give trials number"))
    p = float(input("set probability of success"))
    size = int(input("give output size"))


    s = np.random.binomial(n,p,size)

    #save the binomial distribution 

    np.save("binomial",s)
