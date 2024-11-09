import math


def binomial_coeff(n, k):
    # Функция для вычисления биномиального коэффициента C(n, k)
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def count_paths(n, m, x, y):
    # Количество путей от (1, 1) до (x, y)
    paths_to_mandatory = binomial_coeff(x - 1 + y - 1, x - 1)

    # Количество путей от (x, y) до (n, m)
    paths_from_mandatory = binomial_coeff(n - x + m - y, n - x)

    # Общее количество путей
    return paths_to_mandatory * paths_from_mandatory


# Чтение входных данных
n, m = map(int, input().split())  # Размеры поля
x, y = map(int, input().split())  # Координаты обязательной клетки

# Вычисление и вывод результата
print(count_paths(n, m, x, y))
