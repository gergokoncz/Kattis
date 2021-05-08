def parse(a, m):
    if m == 'h':
        if a == '*':
            return [3600 * i for i in range(24)]
        else:
            ret = []
            hours = a.split(',')
            for h in hours:
                if '-' in h:
                    min, max = map(int, h.split('-'))
                    for k in range(min, max + 1):
                        ret.append(k * 3600)
                else:
                    ret.append(int(h) * 3600)
            return ret
    elif m == 'm':
        if a == '*':
            return [60 * i for i in range(60)]
        else:
            ret = []
            hours = a.split(',')
            for h in hours:
                if '-' in h:
                    min, max = map(int, h.split('-'))
                    for k in range(min, max + 1):
                        ret.append(k * 60)
                else:
                    ret.append(int(h) * 60)
            return ret 
    else:
        if a == '*':
            return [i for i in range(60)]
        else:
            ret = []
            hours = a.split(',')
            for h in hours:
                if '-' in h:
                    min, max = map(int, h.split('-'))
                    for k in range(min, max + 1):
                        ret.append(k)
                else:
                    ret.append(int(h))
            return ret 

if __name__ == '__main__':
    secs = set()
    alljobs = 0
    for _ in range(int(input())):
        h, m, s = input().strip().split()
        ph = parse(h, 'h')
        pm = parse(m, 'm')
        ps = parse(s, 's')
        for h in ph:
            for m in pm:
                for s in ps:
                    secs.add(h + m + s)
        alljobs += len(ph) * len(pm) * len(ps)
    
    print(f"{len(secs)} {alljobs}")