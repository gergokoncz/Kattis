if __name__ == '__main__':
    divisors = 0
    n = int(input())
    c_divisor = 2
    while (c_divisor <= n):
        for i in range(c_divisor, n + 1):
            if n % i == 0:
                n = int(n / i)
                c_divisor = i
                divisors += 1
                break
        if n == 1:
            print(divisors)
        elif c_divisor == n:
            print(divisors + 1)
            break