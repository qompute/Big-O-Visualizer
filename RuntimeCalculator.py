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
plt.scatter(x, y, c='b', label='Bubble sort')

y = test_algorithm(selection_sort, random_list, x)
plt.scatter(x, y, c='r', label='Selection sort')

y = test_algorithm(insertion_sort, random_list, x)
plt.scatter(x, y, c='y', label='Insertion sort')

plt.suptitle('Analysis of Sorting Algorithms')
plt.xlabel('Size of Array (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
