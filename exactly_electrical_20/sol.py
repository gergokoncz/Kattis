if __name__ == "__main__":
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    g = int(input())
    x = a[0] - b[0] if a[0] > b[0] else b[0] - a[0]
    y = a[1] - b[1] if a[1] > b[1] else b[1] - a[1]
    if (y + x) > g or (y + x - g) % 2 != 0:
        print("N")
    else:
        print("Y")
