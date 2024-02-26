import numpy as np
import matplotlib.pyplot as mathplot

def parametric_function(t):
    x = 2 * np.sin(2* t)
    y = 2* np.cos(t)
    return x, y

def graph(x,y):
    mathplot.plot(x, y)
    mathplot.title('Параметрический график функции')
    mathplot.xlabel('x')
    mathplot.ylabel('y')
    mathplot.grid(True)
    mathplot.show()

# Задаем диапазон параметра t
t = np.linspace(0, 2 * np.pi, 100)
# Вызываем функцию для получения значений x и y
x, y = parametric_function(t)
graph(x,y)
