import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 100)

def f(x):
    return sp.sin(x)

def rectangle_method(left, right, n, func):
    dx = (right - left) / n
    area = 0
    x = left
    for i in range(n-1):
        area += dx * func(x)
        x += dx
    return area

def trapezoid_method(left, right, n, func):
    h = (right - left) / n
    area = 0
    x = left
    for i in range(n-1):
        area += h * (func(x) + func(x+h)) / 2
        x += h
    return area

def simpson_method(left, right, n, func):
    h = (right - left) / n
    area = 0
    x = left
    for i in range(n-1):
        area += (func(x) + 4*func(x + h/2) + func(x+h))*(h/6)
        x += h
    return area

def h(y):
    return simpson_method(0, y,100, f)

def h1(y):
   return rectangle_method(0, y, 100, f)

def h2(y):
   return trapezoid_method(0, y, 100, f)

def graph():
    h_val = [h(val) - (1 - math.cos(val)) for val in t]
    h1_val = [h1(val) - (1 - math.cos(val)) for val in t]
    h2_val = [h2(val) - (1 - math.cos(val)) for val in t]
    plt.plot(t, h_val)
    plt.plot(t, h1_val)
    plt.plot(t, h2_val)
    plt.show()

x = sp.Symbol('x')
graph()