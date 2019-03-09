from runtime_calculator import *
from simple_tests import *

"""An iterative quadratic-time function.
"""
def f1(n):
    for i in range(n):
        for j in range(i, n):
            pass

"""An iterative linear-time function.
"""
def f2(n):
    i = 1
    while i < n:
        for j in range(i):
            pass
        i *= 2

"""A logarithmic-time function.
"""
def f3(n):
    if n <= 0:
        return
    for i in range(n % 10):
        pass
    f3(n / 10)

# Expected: N^2
x, y = test_algorithm(f1)
plt.scatter(x, y, c='blue', label='f1')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'b-')
print 'f1:', runtime

# Expected: N
x, y = test_algorithm(f2)
plt.scatter(x, y, c='red', label='f2')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'r-')
print 'f2:', runtime

# Expected: log N
x, y = test_algorithm(f3)
plt.scatter(x, y, c='yellow', label='f3')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'y-')
print 'f3:', runtime

plt.xlabel('Size of Input (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
