class Date:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def addmonths(self, m):
        self.year += int((self.month + m) / 12)
        self.month = (self.month + m) % 12

if __name__ == '__main__':
    s = set()
    a = Date(2018, 3)
    s.add(a.year)
    for _ in range(5000):
        a.addmonths(26)
        s.add(a.year)
    if int(input()) in s:
        print("yes")
    else:
        print("no")
