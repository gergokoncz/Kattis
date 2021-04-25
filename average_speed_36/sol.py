class ElapsedTime:
    def __init__(self, h, m, s):
        self.s = s + 60 * m + 3600 * h
    
    def diff_s(self, other):
        return self.s - other.s

if __name__ == '__main__':
    l = input()
    try:
        t, v = l.strip().split()
        v = int(v)
    except:
        t = l.strip()
        v = 0
        print(f"{t} 0.00 km")
    h, m, s = map(int, t.split(":"))
    distance = 0
    last_time = ElapsedTime(h, m, s)
    while True:
        try:
            l = input()
            if len(l.split()) > 1:
                t, new_v = l.strip().split()
                new_v = int(new_v)
                h, m, s = map(int, t.strip().split(":"))
                new_time = ElapsedTime(h, m, s)
                diff_t = new_time.diff_s(last_time)
                distance += diff_t / 3600 * v
                v = new_v
                last_time = new_time
            else:
                h, m, s = map(int, l.strip().split(":"))
                new_time = ElapsedTime(h, m, s)
                diff_t = new_time.diff_s(last_time)
                distance += diff_t / 3600 * v
                last_time = new_time
                print(f"{l.strip()} {distance:.2f} km")
        except:
            break