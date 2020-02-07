import math

if __name__ == '__main__':
    h, v = map(int, input().split())
    print(math.ceil(h / math.sin(math.radians(v))))

