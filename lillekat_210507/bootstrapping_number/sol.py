if __name__ == '__main__':
    n = int(input())
    var = 0.1
    while var ** var < n:
        var += 1
    while var ** var + 1e-7 > n:
        var -= 1e-7
    print(var)