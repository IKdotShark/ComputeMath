def gause_method(A, B):
    n = len(B)
    for i in range(n):
        # Поиск максимального элемента в столбце для выбора главного элемента
        max_index = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        # Перестановка строк для выбора главного элемента
        A[i], A[max_index] = A[max_index], A[i]
        B[i], B[max_index] = B[max_index], B[i]
        # Приведение матрицы к треугольному виду
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            B[j] -= A[j][i] * X[i]

    return X

A = [[1, 1, 1],
     [1, -1, 2],
     [2, -1, -1]]
B = [6, 5, -3]

solution = gause_method(A, B)
print("Решение системы уравнений:")
for i in range(len(solution)):
    print(f"X{i+1} = {round(solution[i])}")