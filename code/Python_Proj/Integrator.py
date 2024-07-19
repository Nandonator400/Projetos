
##################################### Integrator

import math

def function(x):
    return math.cos(x)

def integrator(func, a, b, step):  # Uses Trapezoidal method
    cnt = a
    area = 0
    while cnt < b:
        try:
            area += step * (func(cnt) + func(cnt+step))/2.0 
            cnt += step
        except ZeroDivisionError:
            cnt += step
    return area

print(integrator(function, -2*math.pi, 2*math.pi,0.0001))

