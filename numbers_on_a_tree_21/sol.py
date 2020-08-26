if __name__ == '__main__':
    # handle input
    r = input().strip()
    if len(r.split(" ")) == 1:
        print(2 ** (int(r) + 1) - 1)
    else:
        h, dirs = r.split()
        h = int(h)
        # build possible list
        mi = 0
        for i in range(h - len(dirs)):
            mi += 2**(h-i)
        ma = mi + 2 ** len(dirs)
        mi = mi + 1
        for idx, c in enumerate(dirs):
            if c == 'L':
                mi += 2**(len(dirs) - idx - 1)
            else:
                ma -= 2**(len(dirs) - idx - 1)
        print(mi)
