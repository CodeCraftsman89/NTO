def max_distance_from_source(n, m, edges, S):
    from collections import defaultdict, deque

    # Создаем граф в виде списка смежности
    graph = defaultdict(list)
    for A, B, d in edges:
        graph[A].append((B, d))

    # Массив для хранения максимальных расстояний
    max_distance = [-1] * (n + 1)
    max_distance[S] = 0

    # Стек для DFS
    stack = [S]
    visited = [False] * (n + 1)

    # Проходим по всем вершинам с помощью DFS
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True

        for neighbor, distance in graph[node]:
            if max_distance[neighbor] < max_distance[node] + distance:
                max_distance[neighbor] = max_distance[node] + distance
                stack.append(neighbor)

    # Убираем индекс 0 и возвращаем результат
    return max_distance[1:]


# Чтение входных данных
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
S = int(input())

# Получаем максимальные расстояния
result = max_distance_from_source(n, m, edges, S)

# Печатаем результат
print(" ".join(map(str, result)))
