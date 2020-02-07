if __name__ == '__main__':
    n, m = raw_input().strip().split()
    w = raw_input().strip().split()
    w = [int(i) for i in w]
    w.sort(reverse = True)
    mongers = [0 for i in range(5000)]
    for _ in range(int(m)):
        x, p = raw_input().split()
        mongers[int(p)] +=  int(x)
    profit = 0
    for f in w[:int(n)]:
        a = len(mongers) - 1
        while mongers[a] == 0:
            del mongers[a]
            a -= 1
        profit += (len(mongers) - 1) * f
        mongers[len(mongers) - 1] -= 1
    print(profit)
