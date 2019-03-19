# Big O Visualizer
A program that (empirically) measures an algorithm's runtime by running it many times with different input sizes.

## Description
This was a simple project created to visualize the [computational complexity](https://en.wikipedia.org/wiki/Computational_complexity) of certain algorithms and see how well they match their expected functions.

## How to Use
All of the functions for calculating runtime complexity are in [`runtime_calculator.py`](runtime_calculator.py). To test the runtime of a particular Python function, you can use:
```python
x, y = test_algorithm(function_to_test)
runtime, fn = find_best_function(x, y)
print(runtime)
```
The `test_algorithm` function will keep running the `function_to_test` function until the total runtime of all function calls exceeds `time_limit` (by default, this is 1 second). You can also specify an `input_generator` to generate an input of size N to this function (for example, if you were to test the efficiency of a function that sorts a list, you might want to generate a list of size N first). The time it takes to generate an input is not counted; only the runtime of the `function_to_test` is recorded.

The `find_best_function` function will find the function that best matches the given data of input sizes and runtimes. Currently, only the following orders of growth are supported:

Function | Name
-------- | ----
Θ(1)     | Constant
Θ(log N) | Logarithmic
Θ(N log N) | Linearithmic
Θ(N<sup>m</sup>) for some integer m | Polynomial
Θ(b<sup>N</sup>) for some integer b | Exponential

The `find_best_function` function uses several linear regression methods to find the curve which best fits the given data. Note that due to the inherent noise present in computer runtimes, the function found empirically for an algorithm may not match its actual computational complexity. In particular, Θ(N) and Θ(N log N) are extremely difficult to differentiate unless N is large. This project is not intended as a replacement for calculating runtimes; it's just a fun way to see how well certain algorithms match their expected average-case complexities!

## Examples
Some examples are given in the files [`simple_tests.py`](simple_tests.py), [`iterative_tests.py`](iterative_tests.py), [`recursive_tests.py`](recursive_tests.py), and [`sorting_tests.py`](sorting_tests.py). We'll show you an example in `sorting_tests.py`.

### Array Sorting
Of course, no introduction to algorithmic runtime complexities would be complete without an analysis of sorting algorithms! The file [`sorting.py`](sorting.py) contains implementations of several common sorting algorithms: [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort), [selection sort](https://en.wikipedia.org/wiki/Selection_sort), [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), [merge sort](https://en.wikipedia.org/wiki/Merge_sort), and [quicksort](https://en.wikipedia.org/wiki/Quicksort). The `sorting_tests.py` file tests each of these sorting algorithms, fits a curve to each of the functions, and prints out its best guess for the runtime complexity of each algorithm. Here's a graph for the runtimes for each function (graph was created using [matplotlib](https://matplotlib.org/)):

![Scatterplot of Sorting Algorithms](/images/sorting-graph.png)

As the graph shows, the quadratic curves fit quite well with the O(N<sup>2</sup>) algorithms (bubble sort, selection sort, and insertion sort). It's quite difficult to tell the runtime complexities of the O(N log N) algorithms, though. We'll try this again but increase the maximum size of N and only show the O(N log N) algorithms:

![Scatterplot of O(N log N) Sorting Algorithms](/images/efficient-sorting-graph.png)

Is it O(N) or O(N log N)? It's hard to tell from a graph; N and N log N are very similar for any reasonable value of N. But we can look at the program output to see which function fits the curve the best, according to `find_best_function`:
```
Bubble sort: N^2
Selection sort: N^2
Insertion sort: N^2
Merge sort: N log N
Quicksort: N log N
```
This matches quite nicely with their expected average-case runtimes! Note that this method is not perfect; sometimes it might misinterpret an N log N algorithm with N, or vice versa. This is why it's better to turn to actual [algorithm analysis](https://en.wikipedia.org/wiki/Analysis_of_algorithms) methods rather than simply running an algorithm thousands of times. But it's interesting to see that the real-world data matches our expectations!

### Other functions
The files [`iterative_tests.py`](iterative_tests.py) and [`recursive_tests.py`](recursive_tests.py) contain some other functions with interesting runtimes, such as this one:
```python
def f1(n):
    if n < 1:
        return
    for _ in range(n):
        pass
    f1(n // 2)
    f1(n // 2)
```
What's the runtime of this function? This is an example of an algorithm whose runtime can be solved with a recurrence relation. (There are many ways of doing this. One way is to use the [master theorem for divide-and-conquer recurrences](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)).) As it turns out, this function has a runtime of Θ(N log N). The `find_best_function` function correctly identifies this as a linearithmic function:

![Scatterplot of Recursive Function f1](/images/f1-graph.png)

See [`iterative_tests.py`](iterative_tests.py) and [`recursive_tests.py`](recursive_tests.py) for more examples like this.
