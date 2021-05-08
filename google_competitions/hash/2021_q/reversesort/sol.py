if __name__ == '__main__':
    for case in range(int(input())):
        l = int(input())
        m = list(map(int, input().split()))
        cost = 0
        for i in range(l - 1):
            min_ind = m.index(min(m[i:]))
            c_cost = min_ind - i + 1
            
            if c_cost == 1:
                cost += c_cost
                continue
            for j in range(c_cost // 2): 
                m[i + j], m[min_ind - j] = m[min_ind - j], m[i + j]

            cost += c_cost

        print(f"Case #{case + 1}: {cost}")