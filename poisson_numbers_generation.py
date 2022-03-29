import numpy as np
import time 


def create_poisson_distribution_numbers_array():


    lamda = int(input("give the lamda"))
    size = int(input("give the size"))


    #tic = time.perf_counter()
    s = np.random.default_rng().poisson(lamda,size)
    #toc = time.perf_counter()

   

   

    print(s.size)
    for i in range(0, len(s)):
        print(s[i])

