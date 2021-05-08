if __name__ == '__main__':
    m = list(map(int, input().split()))
    print(1 if m[0] - 2 >= m[2] and m[1] - 2 >= m[3] else 0)