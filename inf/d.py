# Ввод данных
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Общая площадь поля
total_area = n * m

# Площадь, занятой мамой-ланью
deer_area = (x2 - x1 + 1) * (y2 - y1 + 1)

# Оставшаяся площадь
remaining_area = total_area - deer_area

# Максимальное количество детей
max_children = remaining_area // 2

# Вывод результата
print(max_children)
