# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.

from ast import Return
from contextlib import nullcontext
import numpy as np
import time
import sys
sys.setrecursionlimit(100000)
from collections import Counter


BASELINE = 0
INSERTION_BASELINE = 1 
FIXED_RANDOM = 2  
INSERTION_LIMIT = 32





def insertion_sort(nums):
    print(type(nums),len(nums))
# We start from 1 since the first element is trivially sorted
    for index in range(1, len(nums)):
        currentValue = nums[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and nums[currentPosition - 1] > currentValue:
            nums[currentPosition] = nums[currentPosition -1]
            currentPosition = currentPosition - 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        nums[currentPosition] = currentValue
        
def partition(nums, low, high, sort_mode):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    
    #pivot = nums[int(low + 0.6 * (high - low + 1)) ]
    working_size = high - low + 1
    print(working_size)
    if sort_mode == BASELINE:
        mid_point = (low + high) // 2
    elif sort_mode == INSERTION_BASELINE:
        if working_size  <= INSERTION_LIMIT:
            print("now working size is under the limit")
            print(low,high)
            
            print(type(high), type(low),type(nums))
            insertion_sort(nums[low:high + 1])
            print(nums)
            Return
        else:
            mid_point = (low + high) //2
    elif  sort_mode == FIXED_RANDOM:
        mid_point = int(low + 0.6 * (high - low + 1))
    
    pivot = nums[mid_point]
    #print(low, high, pivot)
    i = low - 1
    j = high + 1
    
    while True:
        
        
        
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        
        
        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]
    
    

def quick_sort(nums):  # Voithitiki sinartisi pou kali ton euato tis
        
        
        def _quick_sort(items, low, high):
            if low < high:
            # This is the index after the pivot, where our lists are split
            #EDO THA eprepe na metrao to partition time?  all pos epistrefei i timi tou xronou gia sigekrimeno partition?
                split_index = partition(items, low, high, 1)
                print(type(low), type(high))  
            
               
                
                
                _quick_sort(items, low,  split_index)
                _quick_sort(items, split_index + 1, high)
                 
        
        _quick_sort(nums, 0, len(nums) - 1)
        
            
    
        





def main():

    #na valo ena menu gia tin epilogi poias katanomis tha kano sort
    #s = np.load("Binomial.npy")
    s = np.load("geometric.npy")
    #s = np.load("Uniform.npy")
    #s = np.load("poisson.npy")
    c = Counter(s)
    #print(c)
    #print(s)
    total = sum(count > 1 for count in c.values())
    print("there are %i duplicates elements in the array " %total)
    #metrisi duplicate dstoixeion kai idion stoixeioon 
    time1 = time.time()
    quick_sort(s)
    time2 = time.time()
    t2=(time2-time1) 
    print('time to sort the array: %f' % t2)
    print('the length of array is ' ,len(s))
    print(s)
    
if (__name__=='__main__'):
    main()




"""

to low ine panta 0!
high - low = high

"""