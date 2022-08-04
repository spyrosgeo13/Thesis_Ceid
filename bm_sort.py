#
#
#  --
#  --
#  --  bm_sort.py: sorting module
#  --
#  --  Use: >>> import bm_sort
#  --
#  --  Arguments: Lowest valid index (start with 0)
#  --             Highest valid index (NOT array length)
#  --
#  --  Methods (defined in that order):
#  --      bm_bubble_sort
#  --      bm_insertion_sort
#  --      bm_quicksort_stack
#  --      bm_quicksort_random
#  --      bm_quicksort_switch - don't use
#  --      bm_quicksort_rec - don't use
#  --      bm_issorted
#  --      bm_test
#  --
#  --  Georgios Drakopoulos 2022
#  --
#  --
#
#

import time
import random
import itertools
import numpy as np
import statistics as st
from enum import Enum
from collections import Counter

class bm_policy(Enum):
    MIDPOINT = 0     #standard midpoint selection (baseline)
    MEDIAN = 1       #median (baseline)
    MID_MEDIAN = 2   #median of a middle section (baseline)
    RANDOM = 3       #uniform random (stochastic baseline)
    CONVEX = 4       #random convex combination
    ALTERNATING = 5  #alternate between 0.4 and 0.6
    #nees politikes gia probipalistic wquicksort
    """1.Median of Medians?
        2. Median of three
        3.Median-of-five with random index selection method
The method employs a sample size of 5 components, including the first, middle, 
and last elements, as well as two more elements chosen at random between the first and 
last elements using a random number generating function. Although this strategy improves load 
balancing and cuts quicksort execution time by more than 5%, there is a cost associated with 
random number creation.?? 
EROTISI: to policy MID_MEDIAN den perni poli xrono?

    """


def bm_bubble_sort(tab, low:int, high:int) -> None:
    """bm_bubble_sort: Basic bubble sort

    """

    sorted = False

    if low < high:
        while not sorted:
            sorted = True
            for i in range(low, high):
                if tab[i] > tab[i+1]:
                    v = tab[i]; tab[i] = tab[i+1]; tab[i+1] = v
                    sorted = False
    return


def bm_insertion_sort(tab, low:int, high:int) -> None:
    """bm_insertion_sort: Insertion sort - simple form

    """

    if low < high:
        for n in range(0,high-low+1):
            for i in range(n,0,-1):
                if tab[i-1] > tab[i]:
                    v = tab[i-1]; tab[i-1] = tab[i]; tab[i] = v
    return


def bm_quicksort_stack(tab, low:int, high:int) -> None:
    """bm_quicksort_stack: Quicksort - stack version

    """

    idx_stack = [(0, -1)]

    if high > low:
        while idx_stack:
            while low < high:
                mid = (low + high)//2
                pivot = tab[mid]
                pivot_elements = [v for v in tab[low:high+1] if v == pivot]
                lower_elements = [v for v in tab[low:high+1] if v < pivot]
                higher_elements = [v for v in tab[low:high+1] if v > pivot]
                new_high = low + len(lower_elements) - 1
                new_low = high - len(higher_elements) + 1
                tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements))
                list.append(idx_stack, (new_low, high))
                high = new_high
            low, high = idx_stack[-1]
            idx_stack = idx_stack[:-1]
    return


def bm_quicksort_random(tab, low:int, high:int, policy:bm_policy=bm_policy.MEDIAN) -> None:
    """bm_quicksort_random: Randomized quicksort with stack

    """

    idx_stack = [(0, -1)]
    mid_elements = 16
    mid_distance = 0.25
    alt_excess = 0.6
    alt_excess_low = True
    pivot_idx = None

    if high > low:
        while idx_stack: #SINEXIZO AN I STOIVA DNE INE KENI
            
            while low < high:

                if bm_policy.MEDIAN == policy:
                    pivot = st.median(tab[low:high+1])
                    pivot_idx = None
                elif bm_policy.MID_MEDIAN == policy:
                    n = high - low + 1
                    if n >= mid_elements:
                        mid_low = int(low + mid_distance*n)
                        mid_high = int(high - mid_distance*n)
                        pivot = st.median(tab[mid_low:mid_high+1])
                    else:
                        pivot = st.median(tab[low:high+1])
                    pivot_idx = None
                elif bm_policy.CONVEX == policy:
                    convex_low = np.random.uniform()
                    pivot_idx = int(convex_low*low + (1-convex_low)*high)
                elif bm_policy.ALTERNATING:
                    pivot_idx = int(alt_excess*low + (1-alt_excess)*high) if alt_excess_low else int(alt_excess*high + (1-alt_excess)*low)
                    alt_excess_low = not alt_excess_low
                elif bm_policy.RANDOM == policy:
                    pivot_idx = int(np.random.uniform(low, 1+high))
                else:
                    pivot_idx = int(low+high)//2
                if pivot_idx:
                    pivot = tab[pivot_idx]
                
                #print("low=",low, "high =",high)
                #print(high-low+1)   

                #partition
                pivot_elements = [v for v in tab[low:high+1] if v == pivot]
                lower_elements = [v for v in tab[low:high+1] if v < pivot]
                higher_elements = [v for v in tab[low:high+1] if v > pivot]
                new_high = low + len(lower_elements) - 1
                new_low = high - len(higher_elements) + 1 #IPOLOGIZO TO LOW ORIO TOU DEXIOU
                tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements)) #ton arxiko pinaka den ton exo piraxei , sinenono ta 3 (voithitaka )dianismata
                list.append(idx_stack, (new_low, high))
                high = new_high #edo pao sto aristero melos
                
                #analoga to vathos sti stoiva epistrefo mikos 
                
            
                
            low, high = idx_stack[-1] # VAZO TO LOW, HIGH STI TELEUTEA DIADA  I DIO AUTES GRAMMER ISODINAMOUN ME POP
            idx_stack = idx_stack[:-1] # OTI EXO IDI STI STOIVA -TIS TELEYTEAS TIMIS
            
    return


def bm_quicksort_switch(tab, low:int, high:int, switch_size:int=32, secondary_sort=bm_insertion_sort) -> None:
    """bm_quicksort_switch: Quicksort switching to secondary sorting function

    """

    idx_stack = [(0, -1)]

    if high > low:
        while idx_stack:
            while low < high:
                if high - low <= switch_size:
                    secondary_sort(tab, low, high)
                    break
                else:
                    mid = (low + high)//2
                    pivot = tab[mid]
                    pivot_elements = [v for v in tab[low:high+1] if v == pivot]
                    lower_elements = [v for v in tab[low:high+1] if v < pivot]
                    higher_elements = [v for v in tab[low:high+1] if v > pivot]
                    if lower_elements:
                        new_high = low + len(lower_elements) - 1
                    else:
                        new_high = low
                    if higher_elements:
                        new_low = high - len(higher_elements) + 1
                    else:
                        new_low = high
                    tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements))
                    list.append(idx_stack, (new_low, high))
                    high = new_high
                    
            low, high = idx_stack[-1]
            idx_stack = idx_stack[:-1]
    return


def bm_quicksort_rec(tab, low:int, high:int) -> None:
    """bm_quickort_rec: Quicksort - recursive version

    """

    if high <= low:
        return
    elif high == 1 + low:
        if tab[low] > tab[high]:
            v = tab[low]; tab[low] = tab[high]; tab[high] = v
    elif (high == 2 + low) or (high == 3 + low) or (high == 4 + low):
        tab[low:high+1] = sorted(tab[low:high+1])
    else:
        mid = (low + high)//2
        pivot = tab[mid]
        pivot_elements = [v for v in tab[low:high+1] if v == pivot]
        lower_elements = [v for v in tab[low:high+1] if v < pivot]
        higher_elements = [v for v in tab[low:high+1] if v > pivot]
        new_high = low + len(lower_elements) - 1
        new_low = high - len(higher_elements) + 1
        tab[low:high+1] = list(itertools.chain(lower_elements, pivot_elements, higher_elements))
        bm_quicksort_rec(tab, low, new_high)
        bm_quicksort_rec(tab, new_low, high)
    return


def bm_issorted(tab) -> bool:
    """bm_issorted: Checks whether an array is sorted.

    """

    n = length(tab)
    for i in range(0, n-1):
        if tab[i] > tab[i+1]:
            return False
    return True

# Driver code
a = np.load("Uniform.npy")
print(a)
#print('the length of array is ' ,len(a))
c = Counter(a)
total = sum(count > 1 for count in c.values())
#print("there are %i duplicates elements in the array " %total)
#metrisi duplicate stoixeion 
time1 = time.time()
bm_quicksort_random(a, 0, len(a) -1)

time2 = time.time()
sort_time=(time2-time1) 
print('time to sort the array: %f' %sort_time)


