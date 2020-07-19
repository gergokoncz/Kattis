if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    a = sorted(a, reverse = True)
    a = [x + idx + 1 for idx, x in enumerate(a)]
    print(max(a) + 1)
