def find_pairs(n, lengths):
    total_length = sum(lengths)
    original_length = total_length // n
    index_map = {}
    pairs = []

    for i, length in enumerate(lengths):
        if original_length - length in index_map:
            pairs.append((index_map[original_length - length] + 1, i + 1))
            del index_map[original_length - length]
        else:
            index_map[length] = i

    return original_length, pairs

# Пример использования
n = int(input())
n2 = input()
lengths = n2.split()
lengths2 = list(map(int, lengths))
original_length, pairs = find_pairs(n, lengths2)
print(original_length)
pairs.sort()
for pair in pairs:
    print(pair[0], pair[1])
