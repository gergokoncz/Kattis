import sys

if __name__ == '__main__':
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(a - b if a > b else b - a)