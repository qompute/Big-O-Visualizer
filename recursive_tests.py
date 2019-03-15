from runtime_calculator import *
from simple_tests import *

"""A recursive linearithmic-time function.
"""
def f1(n):
    if n < 1:
        return
    linear_function(n)
    f1(n // 2)
    f1(n // 2)

"""A recursive exponential-time function.
"""
def f2(n):
    if n < 1:
        return
    f2(n - 1)
    f2(n - 1)

"""A recursive linear-time function.
"""
def f3(n):
    if n < 1:
        return
    for _ in range(1000):
        pass
    f3(n // 2)
    f3(n // 2)

# Expected: N log N
x, y = test_algorithm(f1)
plt.scatter(x, y, c='blue', label='f1')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'b-')
print('f1:', runtime)

# Expected: 2^N
x, y = test_algorithm(f2)
plt.scatter(x, y, c='red', label='f2')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'r-')
print('f2:', runtime)

# Expected: N
x, y = test_algorithm(f3)
plt.scatter(x, y, c='yellow', label='f3')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'y-')
print('f3:', runtime)

plt.xlabel('Size of Input (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()