from sorting import *
from runtime_calculator import *

max_n = 1000
step = 3

x, y = test_algorithm(bubble_sort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='blue', label='Bubble sort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'b-')
print('Bubble sort:', runtime)

x, y = test_algorithm(selection_sort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='red', label='Selection sort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'r-')
print('Selection sort:', runtime)

x, y = test_algorithm(insertion_sort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='yellow', label='Insertion sort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'y-')
print('Insertion sort:', runtime)

x, y = test_algorithm(merge_sort, random_list, step_size=step, max_size=max_n)
plt.scatter(x, y, c='green', label='Merge sort', marker='.')
runtime, func = find_best_function(x, y)
graph_function(plt, x, func, 'g-')
print('Merge sort:', runtime)

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
