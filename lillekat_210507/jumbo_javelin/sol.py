if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        l.append(int(input()))

    print(sum(l) - len(l) + 1)