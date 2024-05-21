import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_eval):
    n = len(x)
    m = len(x_eval)
    interpolated_values = np.zeros(m)

    for i in range(m):
        sum = 0
        for j in range(n):
            term = y[j]
            for k in range(n):
                if k != j:
                    term *= (x_eval[i] - x[k]) / (x[j] - x[k])
            sum += term
        interpolated_values[i] = sum

    return interpolated_values

def graph():
    plt.figure(figsize=(10, 5))
    plt.plot(x_eval, np.abs(x_eval), label='Исходная функция $|x|$')
    plt.plot(x_eval, y_interp_uniform, label='Интерполяция Лагранжа (равномерная сетка)')
    plt.plot(x_eval, y_interp_chebyshev, label='Интерполяция Лагранжа (Чебышевская сетка)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Интерполяция Лагранжа функции $|x|$ на промежутке [-2, 2]')
    plt.legend()
    plt.grid(True)
    plt.show()

# Задаем промежуток
a, b = -2, 2
n = 10  # Узлов интерполяции
x_uniform = np.linspace(a, b, n)
y_uniform = np.abs(x_uniform)

# Создаем узлы интерполяции для Чебышевской сетки
x_chebyshev = (a + b) / 2 + (b - a) / 2 * np.cos((2 * np.arange(1, n + 1) - 1) / (2 * n) * np.pi)
y_chebyshev = np.abs(x_chebyshev)

# Определяем точки, в которых нужно вычислить интерполяцию
x_eval = np.linspace(a, b, 1000)

# Выполняем интерполяцию для равномерной сетки
y_interp_uniform = lagrange_interpolation(x_uniform, y_uniform, x_eval)

# Выполняем интерполяцию для Чебышевской сетки
y_interp_chebyshev = lagrange_interpolation(x_chebyshev, y_chebyshev, x_eval)

graph()