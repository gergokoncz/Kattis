def fz(a):
    if a % 3 == 0 and a % 5 == 0:
        return 'fizzbuzz'
    elif a % 3 == 0:
        return 'fizz'
    elif a % 5 == 0:
        return 'buzz'
    else:
        return str(a)
         
if __name__ == '__main__':
    n, m = map(int, input().split())
    r = []
    for i in range(n):
        l = input().split()
        errs = 0
        #print(l)
        for j in range(1, m+1):
            correct = fz(j)
            #print(correct)
            try:
                #print(l[j - 1])
                if l[j - 1] == correct:
                    continue 
                else:
                    errs += 1
            except:
                errs += 1
        r.append(errs)
    print(r.index(min(r)) + 1)
