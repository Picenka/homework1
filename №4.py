from itertools import permutations

def bananas(s) -> set:
    result = set()

    # Your code here!
    return result


bananas="baa"

list_bananas=list(bananas)
const_list_bananas=list('banana')




list_bananas.append('-')

temp = permutations(list_bananas,len(list_bananas))

for i in list(temp):
    # b=list(i)
    print(i)
    # if "-" in b:
    #     b.remove('-')
    #     print(b)
    #     if str(b) == str(const_list_bananas):
    #        print(b)
    # print (type(i))