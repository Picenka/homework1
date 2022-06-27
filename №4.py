from itertools import combinations


def bananas(s) -> set:
    ba='banana'
    result = set()
    for temp in combinations(range(len(s)), len(s) - len(ba)):
        list_banana = list(s)
        for i in temp:
            list_banana[i] = '-'
        combinations_result = ''.join(list_banana)

        if combinations_result.replace('-', '') == ba:
            result.add(combinations_result)
    print(result)
    return result



assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == { "ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}





