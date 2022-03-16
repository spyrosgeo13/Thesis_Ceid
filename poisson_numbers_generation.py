import numpy as np

def create_poisson_distribution_numbers_array():


    lamda = int(input("give the lamda"))
    size = int(input("give the size"))
    s = np.random.default_rng().poisson(lamda,size)


    

   

    print(s.size)
    for i in range(0, len(s)):
        print(s[i])
