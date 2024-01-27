import timeit
from unicodedata import name
import numpy as np

# This function is same in both iterative and recursive
def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:
  
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)
  
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr,l,h):
  
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
def main():

        # Driver code to test above
        s = np.load("poisson.npy")
        n=len(s)
        print("test")
        print(s)
            #print('Sorted: %s' % quicksort(s, 0, len(s)-1))
            #arr = [4, 3, 5, 2, 1, 3, 2, 3]
            #n = len(arr)
        t1 = timeit.Timer(lambda: quickSortIterative(s, 0, n - 1 )).timeit(number=1)
        print('Time to sort 100000 l floats with quick sort (first element as pivot): %f seconds' % t1)
        print(s)
            #print ("Sorted array is:")
            #for i in range(n):
            #print ("%d" %arr[i])


if (__name__=='__main__'):
    main()

