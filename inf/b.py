from itertools import combinations

# Чтение входных данных
x, y = map(int, input().split())

# Список стоимости вопросов
points = [10, 20, 30, 40, 50]

# Множество для хранения всех возможных результатов
results = set()

# Перебираем все комбинации правильных ответов
for correct in combinations(points, x):
    remaining = set(points) - set(correct)  # Оставшиеся вопросы
    for incorrect in combinations(remaining, y):
        # Считаем итоговый результат
        result = sum(correct) - sum(incorrect)
        results.add(result)

# Выводим результаты в отсортированном порядке
print(*sorted(results))
