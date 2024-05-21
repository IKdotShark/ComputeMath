import numpy as np
import matplotlib.pyplot as mathplot

def graph(x,y):
    mathplot.plot(x, y)
    mathplot.title('График функции')
    mathplot.xlabel('x')
    mathplot.ylabel('y')
    mathplot.grid(True)
    mathplot.show()

def func(t):
    return np.cos(t)

def Right_derivative(t, h):
    return (func(t+h) - func(t)) / h

def Left_derivative(t, h):
    return (func(t) - func(t-h)) / h

def Total_derivative(t , h):
    return (func(t + h) - func(t - h)) / (2 * h)

def Sec_Order_derivative(t, h):
    return (func(t - h) - 2 * func(t) + func(t + h)) / (h ** 2)

def Accurate_Total_derivative(t):
    return -np.sin(t)

def Accurate_Sec_Order_derivative(t):
    return  -np.cos(t)


# Задаем диапазон параметра t
h = 10**-8

t = np.linspace(0, 2 * np.pi, 100)
graph(t, Accurate_Total_derivative(t) - Left_derivative(t,h))
#Accurate_Sec_Order_derivative(t) - Sec_Order_derivative(t, h)
