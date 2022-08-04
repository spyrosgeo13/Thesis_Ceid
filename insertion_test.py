
import numpy as np

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



def main():
    
    s = np.load("Uniform.npy")
    insertion_sort(s)
    print(s)


if (__name__=='__main__'):
    main()
