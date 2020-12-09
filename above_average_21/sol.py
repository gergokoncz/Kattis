if __name__ == '__main__':
    for _ in range(int(input())):
        l = list(map(int, input().split()))
        p = round(sum([1 for x in l[1:] if x > (sum(l[1:]) / l[0])]) * 100 / l[0], 3)
        print(f"{p:.3f}%")
