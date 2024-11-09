def max_plait_area(n, a):
    a.sort(reverse=True)
    half_n = n  //   2
    length1 = sum(a[ : half_n])  #
    length2 = sum(a[half_n : n])
    return length1*length2
n = 8
a = [3, 6, 5, 4, 4, 5, 5, 2]
print(max_plait_area(n, a))
