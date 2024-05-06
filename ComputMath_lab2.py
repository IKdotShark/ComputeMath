def func(x):
    return x ** 2 - 2  # Изначальная функция

def g(x):
    return (x ** 2 + 2) / (2 * x)  # Выразим x из уравнения x = g(x)

def func_derivative(x):
    return 2 * x  # Производная функции f(x)
def dihotomic_method(a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        return None  # Начальные точки должны быть с разными знаками

    for _ in range(max_iter):
        c = (a + b) / 2  # Находим середину отрезка
        if func(c) == 0 or (b - a) / 2 < tol:  # Проверям условие остановки
            return c
        if func(c) * func(a) < 0:  # Проверка знаков функции на концах интервала и в его середине
            b = c
        else:
            a = c

    return (a + b) / 2  # Возвращается среднее значение отрезка

def simple_iteration(x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = g(x)  # Получаем новое приближенное значение
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - func(x) / func_derivative(x)  # Формула метода Ньютона, получаем приближенное значение корня
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Пример использования метода дихотомии
root = dihotomic_method(1, 2)
print("Метод дихотомии:", root)

# Пример использования метода простых итераций
root = simple_iteration(1)
print("Метод простых итераций:", root)

# Пример использования метода Ньютона
root = newton_method(1)
print("Метод Ньютона:", root)

# tol=1e-6 : предел точности/допустимая абсолютная ошибка

# Бояршинов 2006/ч.4/с.27
