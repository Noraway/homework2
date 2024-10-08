def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

# Исходный код
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# Код для создания собственной матрицы
n = int(input('Введите n: '))
m = int(input('Введите m: '))
value = int(input('Введите value: '))
print(get_matrix(n, m, value))