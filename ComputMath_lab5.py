import numpy as np
import matplotlib.pyplot as plt

# Начальные условия
x0 = 1
v0 = 2
t0 = 3
tn = 100
h = 0.1

class easysolution:
    @staticmethod
    def solution1(t):
        return np.sin(t)

    @staticmethod
    def solution2(t):
        return t

    @staticmethod
    def solution3(t):
        return 3 * np.sin(t) / 2 - t * np.cos(t) / 2

class differFunc:
    @staticmethod
    def f1(t, x):
        return -x

    @staticmethod
    def f2(t, x):
        return t - x

    @staticmethod
    def f3(t, x):
        return np.sin(t) - x

def eiler_method(f, x0, v0, t0, tn, h):
    # Список для хранения значений x и v
    x_values = [x0]
    v_values = [v0]
    t_values = [t0]

    # Цикл метода Эйлера
    while t_values[-1] < tn:
        t = t_values[-1]
        x = x_values[-1]
        v = v_values[-1]

        dxdt = v
        dvdt = f(t, x)

        x_new = x + h * dxdt
        v_new = v + h * dvdt
        t_new = t + h

        x_values.append(x_new)
        v_values.append(v_new)
        t_values.append(t_new)

    return t_values, x_values

def graph():
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t_values, x_values1 - solution_values1, label="x''(t) + x(t) = 0")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t_values, x_values2 - solution_values2, label="x''(t) + x(t) = t")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t_values, x_values3 - solution_values3, label="x''(t) + x(t) = sin(t)")
    plt.legend()

    plt.show()

# Вычисляем значения методом Эйлера для каждого уравнения
t_values, x_values1 = eiler_method(differFunc.f1, x0, v0, t0, tn, h)
t_values, x_values2 = eiler_method(differFunc.f2, x0, v0, t0, tn, h)
t_values, x_values3 = eiler_method(differFunc.f3, x0, v0, t0, tn, h)

# Вычисляем значения аналитических функций
solution_values1 = easysolution.solution1(np.array(t_values))
solution_values2 = easysolution.solution2(np.array(t_values))
solution_values3 = easysolution.solution3(np.array(t_values))

graph()
