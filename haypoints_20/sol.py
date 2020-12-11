if __name__ == '__main__':
    n, m = map(int, input().split())
    points = dict()
    for _ in range(n):
        word, val = input().split()
        points[word] = int(val)
    for _ in range(m):
        score = 0
        l = input()
        while l != '.':
            score += sum([points.get(x, 0) for x in l.strip().split()])
            l = input()
        print(score)