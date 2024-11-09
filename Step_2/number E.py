class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        sum_ = 0
        while idx > 0:
            sum_ += self.tree[idx]
            idx -= idx & -idx
        return sum_

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)


def min_energy(n, a):
    max_val = n
    count_tree = FenwickTree(max_val)  # Дерево Фенвика для количества элементов
    sum_tree = FenwickTree(max_val)  # Дерево Фенвика для суммы элементов

    total_energy = 0

    for ai in a:
        # Количество элементов меньше чем текущий ai
        left_count = count_tree.query(ai - 1)
        # Количество элементов больше чем текущий ai
        right_count = count_tree.query(max_val) - count_tree.query(ai)

        # Энергия, если вставлять слева
        left_energy = sum_tree.query(ai - 1)
        # Энергия, если вставлять справа
        right_energy = sum_tree.query(max_val) - sum_tree.query(ai)

        # Выбираем минимальную затрату энергии
        total_energy += min(left_energy, right_energy)

        # Обновляем деревья Фенвика
        count_tree.update(ai, 1)
        sum_tree.update(ai, ai)

    return total_energy


# Ввод
n = int(input())  # Длина перестановки
a = list(map(int, input().split()))  # Перестановка

# Вывод минимальной энергии
print(min_energy(n, a))
