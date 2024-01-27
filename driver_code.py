import bm_sort
import numpy as np
import time
import pandas as pd
import os
#eisagogi tou pinaka pou thelo na kano sorting
dataset = np.load("Distributions_unsorted/Uniform_1000.npy")
print(dataset)
def driver_script(run_times:int):

    for i in range(run_times):


        lista_ipodianismaton = []
        
        time1 = time.time()
        bm_sort.bm_quicksort_random(dataset, 0, len(dataset)-1, lista_ipodianismaton)
        print(lista_ipodianismaton)
        time2 = time.time()
        sort_time = time2 - time1
        ipodistima_nr_1 = lista_ipodianismaton[0] 
        ipodiastima_nr_2 = lista_ipodianismaton[1]
        ipodiastima_nr_3 = lista_ipodianismaton[2]

       
        
    
        #df = pd.DataFrame(data = d)
        df = pd.DataFrame({'plithos stoixeion katanomis' : [len(dataset)], 'xronos katanomis': [sort_time], 'ipodianisma1': [ipodistima_nr_1],'ipodiastima2':[ipodiastima_nr_2], 'ipodiastima3':[ipodiastima_nr_3]})
        print(df)
       
        hdr = False if  os.path.isfile('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_25k.csv') else True
        df.to_csv('C:/Users/spyro/OneDrive/Python_Projects/Thesis_code/csvfiles/poisson_files/poisson_random_25k.csv',mode='a',header=hdr, index=False)
        if bm_sort.bm_issorted(dataset):
            print("ok")
        
driver_script(1000)