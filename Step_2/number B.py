def solve(n, k):
    # Решаем уравнение 2x + (x / k) + (x * k) = n
    # x = n / (2 + 1/k + k)
    x = n / (2 + 1 / k + k)

    # Вычисляем a, b, c, d
    a = int(x - k)
    b = int(x + k)
    c = int(x // k)
    d = int(x * k)

    # Выводим результат
    print(a, b, c, d)


# Чтение входных данных
n, k = map(int, input().split())

# Решение
solve(n, k)
