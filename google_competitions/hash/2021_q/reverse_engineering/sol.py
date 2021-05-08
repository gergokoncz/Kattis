import itertools

if __name__ == '__main__':
    for case in range(int(input())):
        n, c = map(int, input().split())
        if c < (n-1) or c > sum([x for x in range(2, n + 1)]):
            ans = 'IMPOSSIBLE'
        else:
            l = list(range(1, n + 1))
            for c_l in itertools.permutations(l):
                cost = 0
                c_l = list(c_l)
                orig_cl = c_l[:]
                for i in range(n - 1):
                    min_ind = c_l.index(min(c_l[i:]))
                    c_cost = min_ind - i + 1
                    
                    if c_cost == 1:
                        cost += c_cost
                        continue
                    for j in range(c_cost // 2): 
                        c_l[i + j], c_l[min_ind - j] = c_l[min_ind - j], c_l[i + j]

                    cost += c_cost

                if cost == c:
                    l = orig_cl
                    break
            
            
            l = [str(a) for a in l]
            ans = ' '.join(l)

        print(f"Case #{case + 1}: {ans}")