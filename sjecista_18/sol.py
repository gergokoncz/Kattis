if __name__ == '__main__':
    n = int(input())
    dn = n - 3
    if dn % 2 == 0:
        node = 0
        for i in range(int(dn / 2)):
            node += (i+1) * (dn - i)
        print(int(n * node / 2))
    else:
        node = []
        for i in range(int((dn + 1)/2)):
            node.append((i+1) * (dn - i))
        print(int(n * (sum(node) + sum(node[:-1])) / 4))
