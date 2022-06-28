from math import prod
from datetime import datetime

start_time = datetime.now()


def count_find_num(factors: list, max_lim: int) -> list:
    products = [prod(factors)]
    for f in factors:
        for p in products:
            p *= f
            while p <= max_lim and p not in products:
                products.append(p)
                p *= f
    return [len(products), max(products)] if products[0] <= max_lim else []



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


print(datetime.now() - start_time)