def can_cut_squares(x, a, b, c, d):
    # Количество квадратов из первого прямоугольника
    count1 = (a // x) * (b // x)
    # Количество квадратов из второго прямоугольника
    count2 = (c // x) * (d // x)
    return count1 + count2 >= 2


def max_square_size(a, b, c, d):
    left, right = 0, min(a, b, c, d)

    while right - left > 1e-7:  # точность до 1e-7
        mid = (left + right) / 2
        if can_cut_squares(mid, a, b, c, d):
            left = mid  # можем увеличить размер
        else:
            right = mid  # уменьшаем размер

    return left

def can_convert_without_loss(value):
    return value == int(value)

# Ввод данных
a, b = map(int, input().split())
c, d = map(int, input().split())

# Получаем максимальный размер квадрата
result = max_square_size(a, b, c, d)

# Вывод результата с точностью 1 знак после запятой
if can_convert_without_loss(result) == True:
    print(int(result))
else:
    print(f"{result:.1f}")