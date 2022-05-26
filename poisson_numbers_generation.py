import numpy as np
import time 
import QuickSort2
from collections import Counter


def create_poisson_distribution_numbers_array():

    
    lamda = int(input("give the lamda"))
    size = int(input("give the size"))


    # creating the array s
    s = np.random.poisson(lamda,size)
    
    #store the  created array in a file 
    np.save("poisson.npy", s)

def load_poisson_distribution_and_sort_it():
    #calling this we can sort and view details of the distribution
    s = np.load("poisson.npy")
    c = Counter(s)
    print(c)
    #metrisi duplicate dstoixeion kai idion stoixeioon 
    time1 = time.time()
    QuickSort2.quick_sort(s)
    time2 = time.time()
    t2=(time2-time1) 
    print('time to sort the array: %f' % t2)
    print('the length of array is ' ,len(s))
    print(s)
