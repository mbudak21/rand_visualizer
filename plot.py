import matplotlib.pyplot as plt
import math

start = 0
end = 10
n = 10000

def f_expo(x):
    return x ** 2

def graph(start, end, f, n):
    x_values = []
    y_values = []
    
    step = (end - start) / n
    x = start
    while x <= end:
        x_values.append(x)
        y_values.append(f(x))
        x += step
        
    return x_values, y_values

x_vals, y_vals = graph(start, end, math.sin, n)
# Plotting
plt.plot(x_vals, y_vals, label='y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x^2')
plt.legend()
plt.grid(True)
plt.show()