from itertools import permutations
from collections import Counter

if __name__ == '__main__':
    for i in range(50):
        ds = list()
        for perm in permutations(range(i)):
            d = 0
            for i in range(len(perm) - 1):
                if perm[i+1] < perm[i]:
                    d += 1
            ds.append(d)
        print(Counter(ds))
