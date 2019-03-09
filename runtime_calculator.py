import time
import math
import matplotlib.pyplot as plt

"""The identity function.
"""
identity = lambda n: n

""" Tests the runtime of a given function by repeating many trials.
"""
def test_algorithm(function, input_generator=identity, min_size=1,
            step_size=1, time_limit=1):
    input_sizes, speeds = [], []
    n, total_time = min_size, 0
    while total_time < time_limit:
        n += step_size
        args = input_generator(n)
        start = time.time()
        function(args)
        end = time.time()
        elapsed_time = end - start
        if elapsed_time > 0:
            input_sizes.append(n)
            speeds.append(elapsed_time)
            total_time += elapsed_time
    return input_sizes, speeds

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
    if power == 0:
        complexity = '1'
        constant, _, r2 = linear_regression(x, y)
        function = lambda x: constant
    else:
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
