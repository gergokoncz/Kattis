if __name__ == '__main__':
    n, m = map(int, input().split())
    ways = {}
    for i in range(n):
        ways[i] = dict()
    for _ in range(m):

