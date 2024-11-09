# Входные данные
a, b, c, d = map(int, input().split())  # Количество жёлтых, зелёных, красных и синих треугольников
n, m = map(int, input().split())  # Размеры таблицы

# Максимальное количество ячеек в таблице
max_cells = n * m

# Количество пар треугольников
yellow_red_pairs = min(a, c)  # Пары жёлтых и красных
green_blue_pairs = min(b, d)  # Пары зелёных и синих

# Сколько пар можно разместить в таблице
pairs_count = yellow_red_pairs + green_blue_pairs

# Оставшиеся одиночные треугольники
remaining_yellow = a - yellow_red_pairs
remaining_red = c - yellow_red_pairs
remaining_green = b - green_blue_pairs
remaining_blue = d - green_blue_pairs

# Оставшиеся одиночные треугольники
remaining_triangles = remaining_yellow + remaining_red + remaining_green + remaining_blue

# Сколько ячеек осталось после размещения пар
remaining_cells = max_cells - 2 * pairs_count

# Сколько всего треугольников можно разместить
max_placed_triangles = 2 * pairs_count + min(remaining_triangles, remaining_cells)

# Вывод результата
print(max_placed_triangles)
