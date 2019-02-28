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

"""Performs a least-squares linear regression on x and y.
Returns the y-intercept, the slope, and the coefficient of determination.
"""
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

"""Finds the best function to fit the given data.
"""
def find_best_function(x, y):
    log_x = [math.log(i) for i in x]
    log_y = [math.log(i) for i in y]

    _, power, _ = linear_regression(log_x, log_y)
    power = int(round(power))
    x_power = [i ** power for i in x]
    _, coefficient, _ = linear_regression(x_power, y)
    return lambda x: coefficient * x ** power

"""Graphs a function on a given pyplot.
"""
def graph_function(plt, x, f, color):
    y = []
    for input in x:
        y.append(f(input))
    plt.plot(x, y, color)

x = range(1, 500, 2)

y = test_algorithm(bubble_sort, random_list, x)
plt.scatter(x, y, c='blue', label='Bubble sort')
graph_function(plt, x, find_best_function(x, y), 'b-')

y = test_algorithm(selection_sort, random_list, x)
plt.scatter(x, y, c='red', label='Selection sort')
graph_function(plt, x, find_best_function(x, y), 'r-')

y = test_algorithm(insertion_sort, random_list, x)
plt.scatter(x, y, c='yellow', label='Insertion sort')
graph_function(plt, x, find_best_function(x, y), 'y-')

y = test_algorithm(merge_sort, random_list, x)
plt.scatter(x, y, c='green', label='Merge sort')
graph_function(plt, x, find_best_function(x, y), 'g-')

y = test_algorithm(quicksort, random_list, x)
plt.scatter(x, y, c='magenta', label='Quicksort')
graph_function(plt, x, find_best_function(x, y), 'm-')

plt.suptitle('Analysis of Sorting Algorithms')
plt.xlabel('Size of Array (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
