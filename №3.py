def zeros(n):
    a = 0
    while n // 5 != 0:
        a = a + n // 5
        n = n // 5
    return a


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
