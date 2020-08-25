def reverse(a, b, c, d):
    a.reverse()
    b.reverse()
    c.reverse()
    d.reverse()
    return a, b, c, d

def transpose(a, b, c, d):
    e = [x[0] for x in [a, b, c, d]]
    f = [x[1] for x in [a, b, c, d]]
    g = [x[2] for x in [a, b, c, d]]
    h = [x[3] for x in [a, b, c, d]]
    return e, f, g, h

def trans(a, b, c, d, m, o):
    ## transform according to direction
    if m == 2:
        a, b, c, d = reverse(a, b, c, d)
    
    if m == 1:
        a, b, c, d = transpose(a, b, c, d)

    if m == 3:
        if o == 0:
            a, b, c, d = transpose(a, b, c, d)
            a, b, c, d = reverse(a, b, c, d)
        else:
            a, b, c, d = reverse(a, b, c, d)
            a, b, c, d = transpose(a, b, c, d)

    return a, b, c, d

def summ(a, b, c, d):
    for x in [a, b, c, d]:
        transformable = [True, True, True, True]
        for i in range(1, 4):
            for j in range(i):
                move, cond = x[i-j], x[i-j-1]
                if cond == 0:
                    x[i-j-1] = x[i-j]
                    x[i-j] = 0
                elif cond == move and transformable[i-j-1]:
                    x[i-j-1] = 2 * move
                    x[i-j] = 0
                    transformable[i-j-1] = False
                    break
                else:
                    break
    return a, b, c, d

if __name__ == '__main__':
    # read input
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))
    d = list(map(int, input().split(' ')))
    m = int(input()) # 0:left 1:up 2:right 3:down

    a, b, c, d = trans(a, b, c, d, m, 0)
    a, b, c, d = summ(a, b, c, d)
    a, b, c, d = trans(a, b, c, d, m, 1)
    for x in [a, b, c, d]:
        x = [str(y) for y in x]
        print(" ".join(x))
