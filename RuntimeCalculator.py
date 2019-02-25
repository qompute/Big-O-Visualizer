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

def linear_regression(x, y):
    meanX = sum(x) / len(x)
    meanY = sum(y) / len(y)
    ss_xx = sum([(i - meanX) * (i - meanX) for i in x])
    ss_yy = sum([(i - meanY) * (i - meanY) for i in y])
    ss_xy = sum([(x[i] - meanX) * (y[i] - meanY) for i in range(len(x))])

    b = ss_xy / ss_xx
    a = meanY - b * meanX
    r_squared = ss_xy * ss_xy / (ss_xx * ss_yy)
    return a, b, r_squared

def draw_line(plt, x, y, color):
    line = linear_regression(x, y)
    end = max(x)
    plt.plot((0, end), (line[0], line[1] * end), color)

x = range(1, 500, 2)

y = test_algorithm(bubble_sort, random_list, x)
plt.scatter(x, y, c='blue', label='Bubble sort')
draw_line(plt, x, y, 'b-')

y = test_algorithm(selection_sort, random_list, x)
plt.scatter(x, y, c='red', label='Selection sort')
draw_line(plt, x, y, 'r-')

y = test_algorithm(insertion_sort, random_list, x)
plt.scatter(x, y, c='yellow', label='Insertion sort')
draw_line(plt, x, y, 'y-')

y = test_algorithm(merge_sort, random_list, x)
plt.scatter(x, y, c='green', label='Merge sort')
draw_line(plt, x, y, 'g-')

y = test_algorithm(quicksort, random_list, x)
plt.scatter(x, y, c='magenta', label='Quicksort')
draw_line(plt, x, y, 'm-')

plt.suptitle('Analysis of Sorting Algorithms')
plt.xlabel('Size of Array (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
