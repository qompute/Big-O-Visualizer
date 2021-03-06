from sorting import *
from runtime_calculator import *

max_n = 5000
step = 9

x, y = test_algorithm(merge_sort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='green', label='Merge sort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'g-')
print('Merge sort:', runtime)

x, y = test_algorithm(heapsort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='blue', label='Heapsort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'b-')
print('Heapsort:', runtime)

x, y = test_algorithm(quicksort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='magenta', label='Quicksort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'm-')
print('Quicksort:', runtime)

plt.suptitle('Analysis of Efficient Sorting Algorithms')
plt.xlabel('Size of Array (N)')
plt.ylabel('Runtime (seconds)')
plt.legend(loc='upper left')
plt.show()
