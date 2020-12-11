if __name__ == '__main__':
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    w = sorted(w)
    
    mon_dict = dict()
    price_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        mon_dict[b] = mon_dict.get(b, 0) + a
        price_list.append(b)

    profit = 0
    price_list = sorted(price_list, reverse=True)
    for price in price_list:
        to_sell = mon_dict.get(price)
        if to_sell < n:
            profit += price * sum(w[n-to_sell:n])
            n -= to_sell
        else:
            profit += price * sum(w[:n])
            break
    print(profit)