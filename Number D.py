def total_details(purchased, a, b):
    # Подсчет общего количества деталей
    total = purchased
    free = purchased // b  # бесплатные заготовки
    scraps = purchased  # остатки стружек

    while free > 0 or scraps >= a:
        # Добавляем бесплатные заготовки
        total += free
        scraps += free

        # Перерабатываем стружки в новые заготовки
        new_from_scraps = scraps // a
        total += new_from_scraps

        # Обновляем количество бесплатных заготовок и остатков стружек
        free = new_from_scraps // b
        scraps = scraps % a + new_from_scraps

    return total


def min_purchased(a, b, c):
    left, right = 0, c

    while left < right:
        mid = (left + right) // 2
        if total_details(mid, a, b) >= c:
            right = mid  # ищем меньшее количество
        else:
            left = mid + 1  # ищем большее количество

    return left


# Чтение входных данных
a, b, c = map(int, input().strip().split())

# Вывод результата
print(min_purchased(a, b, c))