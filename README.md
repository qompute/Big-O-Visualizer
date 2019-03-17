# Big O Visualizer
A program that (empirically) measures an algorithm's runtime by running it many times with different input sizes.

## Description
This was a simple project created to visualize the [computational complexity](https://en.wikipedia.org/wiki/Computational_complexity) of certain algorithms and see how well they match their expected functions.

## How to Use
All of the functions for calculating runtime complexity are in `runtime_calculator.py`. To test the runtime of a particular Python function, you can use:
```python
x, y = test_algorithm(function_to_test)
runtime, fn = find_best_function(x, y)
print(runtime)
```
The `test_algorithm` function will keep running the `function_to_test` function until the total runtime of all function calls exceeds `time_limit` (by default, this is 1 second). You can also specify an `input_generator` to generate an input of size N to this function (for example, if you were to test the efficiency of a function that sorts a list, you might want to generate a list of size N first). The time it takes to generate an input is not counted; only the runtime of the `function_to_test` is recorded.

The `find_best_function` function will find the function that best matches the given data of input sizes and runtimes. Currently, only the following complexities are supported:

Function | Name
-------- | ----
Θ(1)     | Constant
Θ(log N) | Logarithmic
Θ(N log N) | Linearithmic
Θ(N<sup>m</sup>) for some integer m | Polynomial
Θ(b<sup>N</sup>) for some integer b | Exponential

The `find_best_function` uses several linear regression methods to find the curve which best fits the given data. Note that due to the inherent noise present in computer runtimes, the function found empirically for an algorithm may not match its actual computational complexity. In particular, Θ(N) and Θ(N log N) are extremely difficult to differentiate unless N is large. This project is not intended as a replacement for calculating runtimes; it's just a fun way to see how well certain algorithms match their expected average-case complexities!
