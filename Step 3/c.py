def area_difference(n1, n2, n3, n4):
    total_area = n1 * n2
    part1_1 = (n3 * n4) / 2
    part1_2 = total_area - part1_1
    diff1 = abs(part1_1 - part1_2)
    part2_1 = ((n1 - n3) * n4) / 2
    part2_2 = total_area - part2_1
    diff2 = abs(part2_1 - part2_2)
    part3_1 = ((n1 - n3) * (n2 - n4)) / 2
    part3_2 = total_area - part3_1
    diff3 = abs(part3_1 - part3_2)


    part4_1 = (n3 * (n2 - n4)) / 2
    part4_2 = total_area - part4_1
    diff4 = abs(part4_1 - part4_2)

    return min(diff1, diff2, diff3, diff4)

num1, num2 = map(int, input().split())
num3, num4 = map(int, input().split())

result = area_difference(num1, num2, num3, num4)

print(f"{result:.3f}")
