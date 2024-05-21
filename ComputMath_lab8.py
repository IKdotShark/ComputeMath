import random
import numpy as np

def main():
    # Генерация большого массива псевдослучайных чисел
    random.seed(42)  # Установка seed для воспроизводимости результатов
    n = 1000000  # Количество сгенерированных чисел
    random_numbers = [random.random() for _ in range(n)]

    # Поиск повторяющихся последовательностей из первых пяти чисел
    sequence_to_find = random_numbers[:5]
    count = 0
    for i in range(len(random_numbers) - 5):
        if random_numbers[i:i+5] == sequence_to_find:
            count += 1

    print("Количество повторений первых пяти чисел:", count)

    # Вычисление математического ожидания и дисперсии
    mean = np.mean(random_numbers)
    variance = np.var(random_numbers)

    print("Математическое ожидание:", mean)
    print("Дисперсия:", variance)

    # Создание дискретной случайной величины с заданными значениями и вероятностями
    values = [1, 2, 3, 4, 5]
    probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]

    # Генерация случайной величины с использованием заданных значений и вероятностей
    # discrete_random_variable = np.random.choice(values, p=probabilities)

    #print("Случайная величина с заданными значениями и вероятностями:", discrete_random_variable)

    # Вычисление вероятностей для каждого значения дискретной случайной величины
    num_samples = 10000  # Количество сгенерированных значений для оценки вероятностей
    #samples = np.random.choice(values, size=num_samples, p=probabilities)
    #unique, counts = np.unique(samples, return_counts=True)
    #probability_dict = dict(zip(unique, counts / num_samples))

   #print("Вероятности для каждого значения дискретной случайной величины:")
    #for value, probability in probability_dict.items():
    #    print(f"Значение: {value}, Вероятность: {probability}")

    cumulative_prob = 0
    random_value = random.random()
    discrete_random_variable = 0

    # Выбор значения дискретной случайной величины на основе вероятностей
    for i in range(len(values)):
        value = values[i]
        prob = probabilities[i]
        cumulative_prob += prob
        if cumulative_prob >= random_value:
            discrete_random_variable = value
            break

    print("Дискретная случайная величина с заданными значениями и вероятностями:", discrete_random_variable)

if __name__ == "__main__":
    main()