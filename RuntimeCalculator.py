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

    # Polynomial
    _, power, _ = linear_regression(log_x, log_y)
    power = int(round(power))
    x_power = [i ** power for i in x]
    _, multiplier, r2 = linear_regression(x_power, y)
    if power == 1:
        complexity = 'N'
    else:
        complexity = 'N^' + str(power)
    coefficient = multiplier
    function = lambda x: coefficient * x ** power

    # Exponential
    _, base, _ = linear_regression(x, log_y)
    base = int(round(math.exp(base)))
    if base > 1:
        x_exp = [base ** i for i in x]
        _, multiplier, new_r2 = linear_regression(x_exp, y)
        if new_r2 > r2:
            coefficient = multiplier
            function = lambda x: coefficient * base ** x
            if base == 1:
                complexity = '1'
            else:
                complexity = str(base) + '^N'

    # Logarithmic
    _, multiplier, new_r2 = linear_regression(log_x, y)
    if new_r2 > r2:
        coefficient = multiplier
        function = lambda x: coefficient * math.log(x)
        complexity = 'log N'

    # Linearithmic
    x_log_x = [i * math.log(i) for i in x]
    _, multiplier, new_r2 = linear_regression(x_log_x, y)
    if new_r2 > r2:
        coefficient = multiplier
        function = lambda x: coefficient * x * math.log(x)
        complexity = 'N log N'

    return complexity, function

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
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'b-')
print 'Bubble sort:', runtime

y = test_algorithm(selection_sort, random_list, x)
plt.scatter(x, y, c='red', label='Selection sort')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'r-')
print 'Selection sort:', runtime

y = test_algorithm(insertion_sort, random_list, x)
plt.scatter(x, y, c='yellow', label='Insertion sort')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'y-')
print 'Insertion sort:', runtime

y = test_algorithm(merge_sort, random_list, x)
plt.scatter(x, y, c='green', label='Merge sort')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'g-')
print 'Merge sort:', runtime

y = test_algorithm(quicksort, random_list, x)
plt.scatter(x, y, c='magenta', label='Quicksort')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'm-')
print 'Quicksort:', runtime

plt.suptitle('Analysis of Sorting Algorithms')
plt.xlabel('Size of Array (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
