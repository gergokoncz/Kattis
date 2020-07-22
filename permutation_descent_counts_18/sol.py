from itertools import permutations

if __name__ == '__main__':
    for _ in range(int(input()) - 1):
        ans = 0
        l = list(map(int, input().split(" ")))
        for perm in permutations(range(l[1])):
            d = 0
            for i in range(len(perm) - 1):
                if perm[i + 1] < perm[i]:
                    d += 1
                    if d > l[2]:
                        break
            if d == l[2]:
                ans += 1
        print("{} {}".format(l[0], ans))
