from math import *
from runtime_calculator import *

"""Creates a function whose runtime equals the given runtime function.
"""
def create_function(runtime_function):
    def f(n):
        for _ in range(runtime_function(n)):
            pass
    return f


# Expected: Linear time algorithm
x, y = test_algorithm(create_function(lambda n: 5 * n))
plt.scatter(x, y, c='blue', label='Linear')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'b-')
print 'Linear Time Algorithm:', runtime

# Expected: Quadratic time algorithm
x, y = test_algorithm(create_function(lambda n: n * n))
plt.scatter(x, y, c='red', label='Quadratic')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'r-')
print 'Quadratic Time Algorithm:', runtime

# Expected: Linearithmic time algorithm
x, y = test_algorithm(create_function(lambda n: n * int(log(n))))
plt.scatter(x, y, c='yellow', label='Linearithmic')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'y-')
print 'Linearithmic Time Algorithm:', runtime


plt.xlabel('Size of Input (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
