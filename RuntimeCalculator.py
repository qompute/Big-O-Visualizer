import time
import math
import matplotlib.pyplot as plt
from sorting import *

""" Tests the runtime of a given function by repeating many trials.
"""
def test_algorithm(function, input_generator, size_range):
    speeds = []
    for n in size_range:
        args = input_generator(n)
        start = time.time()
        function(args)
        end = time.time()
        speeds.append(end - start)
    return speeds

x = range(1, 500, 2)

y = test_algorithm(bubble_sort, random_list, x)
plt.scatter(x, y, c='blue', label='Bubble sort')

y = test_algorithm(selection_sort, random_list, x)
plt.scatter(x, y, c='red', label='Selection sort')

y = test_algorithm(insertion_sort, random_list, x)
plt.scatter(x, y, c='yellow', label='Insertion sort')

y = test_algorithm(merge_sort, random_list, x)
plt.scatter(x, y, c='green', label='Merge sort')

y = test_algorithm(quicksort, random_list, x)
plt.scatter(x, y, c='purple', label='Quicksort')

plt.suptitle('Analysis of Sorting Algorithms')
plt.xlabel('Size of Array (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
