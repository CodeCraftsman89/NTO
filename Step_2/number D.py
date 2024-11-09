def swap_pairs(s):
    # Меняем местами соседние пары символов
    lst = list(s)
    for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
    return ''.join(lst)


def find_max_min_difference(A):
    n = len(A)
    seen = set()
    min_value = float('inf')
    max_value = -float('inf')

    # Перебираем все ротации числа
    for i in range(n):
        rotated = A[i:] + A[:i]

        # Меняем соседние пары
        swapped = swap_pairs(rotated)

        # Преобразуем результат в число
        num = int(swapped)

        # Обновляем максимальное и минимальное число
        min_value = min(min_value, num)
        max_value = max(max_value, num)

    # Возвращаем разницу между максимальным и минимальным числом
    return max_value - min_value


# Ввод
A = input().strip()

# Вывод результата
print(find_max_min_difference(A))
