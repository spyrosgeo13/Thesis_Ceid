import random
import numpy as np
import sys
sys.setrecursionlimit(100000)


def quicksort(arr, start, end, pivot_mode='random'):
	if start < end:
		split = partition(arr, start, end, pivot_mode)
		quicksort(arr, start, split-1, pivot_mode)
		quicksort(arr, split+1, end, pivot_mode)
	return arr

def partition(arr, start, end, pivot_mode):
	if pivot_mode == 'first':
		pivot = arr[start]
	else:
		pivot_index = random.randrange(start,end)
		pivot = arr[pivot_index]
		arr[pivot_index], arr[start] = arr[start], arr[pivot_index] # place the pivot at the beginning
	i = start + 1
	for j in range(start+1,end+1):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[start], arr[i-1] = arr[i-1], arr[start]
	return i-1

def main():
	
	import timeit
	# One example to visually check that sorting works
	s = np.load("poisson.npy")
	print('Not sorted: %s' % s)
	print(len(s))
	print('Sorted: %s' % quicksort(s, 0, len(s)-1))
	print("test")
	# Comparison between quick sort (both with pivot as the first element and random pivot) and the built-in Python sort
	big_arr = [random.random() for _ in range(100000)]
	t1 = timeit.Timer(lambda: quicksort(s, 0, len(s)-1, 'first')).timeit(number=1)
	big_arr = [random.random() for _ in range(100000)]
	t2 = timeit.Timer(lambda: quicksort(big_arr, 0, len(big_arr)-1, 'random')).timeit(number=1)
	big_arr = [random.random() for _ in range(100000)]
	t3 = timeit.Timer(lambda: sorted(big_arr)).timeit(number=1)
	print('Time to sort 100000 l floats with quick sort (first element as pivot): %f seconds' % t1)
	print('Time to sort 100000 floats with quick sort (random pivot): %f seconds' % t2)
	print('Time to sort 100000 floats with python built-in sort : %f seconds' % t3)
	print('Ratio 1stquick/built-in: %f' % (t1/t3))
	#print('Ratio 2ndquick/built-in: %f' % (t2/t3))
	
if (__name__ == '__main__'):
	main()