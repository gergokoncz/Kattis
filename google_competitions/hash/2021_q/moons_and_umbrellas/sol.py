if __name__ == '__main__':
    for case in range(int(input())):
        cost = 0
        l = input().strip().split()
        x = int(l[0])
        y = int(l[1])
        a = True if x > y else False
        t = l[2].replace('?', '')
        for i, c in enumerate(t[:-1]):
            if c == 'C':
                if t[i + 1] == 'J':
                    cost += x
            elif c == 'J':
                if t[i + 1] == 'C':
                    cost += y


        print(f"Case #{case + 1}: {cost}")