from collections import Counter
from msilib import type_short
import time 
import numpy as np

from QuickSort2 import FIXED_RANDOM



BASELINE_PIVOT = 0
FIXED_PIVOT = 1
INSERTION_LIMIT = 10





# Function to perform the insertion sort
def insertion_sort(arr):
    
    print("insertion started")
# We start from 1 since the first element is trivially sorted
    for index in range(1, len(arr)):
        currentValue = arr[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and arr[currentPosition - 1] > currentValue:
            arr[currentPosition] = arr[currentPosition -1]
            currentPosition = currentPosition - 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        arr[currentPosition] = currentValue
 
# The following two functions are used
# to perform quicksort on the array.
 
# Partition function for quicksort
def partition(arr, low, high, sort_mode):
    if sort_mode == BASELINE_PIVOT:
        pivot = arr[high-low //2]
        i = j = low
        for i in range(low, high):
            if arr[i]<pivot:
                a[i], a[j]= a[j], a[i]
                j+= 1
        a[j], a[high]= a[high], a[j]
        return j
    elif sort_mode == FIXED_PIVOT:
        pivot = arr[int(low + 0.6 * (high - low + 1))]
        i = j = low 
        for i in range(low, high):
            if arr[i]<pivot:
                a[i], a[j]= a[j], a[i]
                j+= 1
        a[j], a[high]= a[high], a[j]
        return j
 
# Function to call the partition function
# and perform quick sort on the array
def quick_sort(arr, low, high):
    if low<high:
        pivot = partition(arr, low, high, 0)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
        return arr
 
# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
    while low<high:
 
        # Ean to megethos tou pinaka ine mikrotero tou Limit tote kanoume insertion sort
        if high-low + 1< INSERTION_LIMIT:
            insertion_sort(arr)
            break
 
        else:
            pivot = partition(arr, low, high, 0)
 
            if pivot-low<high-pivot:
                hybrid_quick_sort(arr, low, pivot-1)
                low = pivot + 1
            else:
                
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot-1
 
# Driver code
a = np.load("Uniform.npy")
c = Counter(a)
print(c)
total = sum(count > 1 for count in c.values())
print("there are %i duplicates elements in the array " %total)
#metrisi duplicate stoixeion 
time1 = time.time()
hybrid_quick_sort(a, 0, len(a) -1)
time2 = time.time()
sort_time=(time2-time1) 
print('time to sort the array: %f' %sort_time)
print('the length of array is ' ,len(a))
print(a)