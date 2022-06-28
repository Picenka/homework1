

def count_find_num(primes, max_lim):
    primes_prod = 1

    for p in primes:
        primes_prod *= p
    steps = max_lim // primes_prod
    count = 0
    max_n = 0
    for i in range(1, steps + 1):
        x = i
        for p in primes:
            while x % p == 0:
                x //= p
        if x == 1:
            count = 1+count
            max_n = i * primes_prod
    if count == 0:
        return []
    print(count,max_n)
    return [count, max_n]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

primesL = [2, 5, 7]
limit = 500
count_find_num(primesL, limit)