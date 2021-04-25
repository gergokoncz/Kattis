if __name__ == '__main__':
    for case in range(int(input())):
        l = int(input())
        m = [list(map(int, input().split())) for _ in range(l)]
        # trace calc
        k = sum([m[i][i] for i in range(l)])
        # row
        r = sum([len(row) != len(set(row)) for row in m])
        # col
        c = sum([len([row[i] for row in m]) != len(set([row[i] for row in m])) for i in range(l)])
        print(f"Case #{case + 1}: {k} {r} {c}")