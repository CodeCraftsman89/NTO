import math

def find_grid_dimensions(num1, num2):
    if num2 == 0:
        return 1, 1
    for num in range(1, int(math.sqrt(num2)) + 2):
        if num == 1:
            continue
        if num2 % (num - 1) == 0:
            m = num2 // (num - 1) + 1
            if 2 * (num + m - 2) == num1:
                return num, m
    return None

a, b = map(int, input().split())

result = find_grid_dimensions(a, b)

if result:
    n, m = result
    if n > m:
        n, m = m, n
    print(n, m)

