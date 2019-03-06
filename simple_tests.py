from runtime_calculator import *

"""A function that has O(N) time complexity.
"""
def linear_function(n):
    for _ in range(n):
        pass

"""A function that has O(N log N) time complexity.
"""
def linearithmic_function(n):
    for _ in range(n):
        i = 1
        while i < n:
            i *= 2

"""A function that has O(N^2) time complexity.
"""
def quadratic_function(n):
    for _ in range(n):
        for _ in range(n):
            pass

# # Expected: Linear time algorithm
# x, y = test_algorithm(linear_function)
# plt.scatter(x, y, c='blue', label='Linear')
# runtime, func = find_best_function(x, y)
# graph_function(plt, x, func, 'b-')
# print 'Linear Time Algorithm:', runtime
#
# # Expected: Quadratic time algorithm
# x, y = test_algorithm(quadratic_function)
# plt.scatter(x, y, c='red', label='Quadratic')
# runtime, func = find_best_function(x, y)
# graph_function(plt, x, func, 'r-')
# print 'Quadratic Time Algorithm:', runtime
#
# # Expected: Linearithmic time algorithm
# x, y = test_algorithm(linearithmic_function)
# plt.scatter(x, y, c='yellow', label='Linearithmic')
# runtime, func = find_best_function(x, y)
# graph_function(plt, x, func, 'y-')
# print 'Linearithmic Time Algorithm:', runtime
#
#
# plt.xlabel('Size of Input (N)')
# plt.ylabel('Runtime (seconds)')
# plt.legend(loc='upper left')
# plt.show()
