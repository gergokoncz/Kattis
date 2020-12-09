if __name__ == '__main__':
    n, time = map(int, input().split())
    values = [[] for i in range(time)]
    for _ in range(n):
        value, c_t = map(int, input().split())
        if c_t >= time:
            c_t = time - 1
        values[c_t].append(value)
    
    for idx, l in enumerate(values):
        values[idx] = sorted(values[idx], reverse=True)
        if len(values[idx]) < (idx + 1):
            values[idx] = values[idx] + [0 for _ in range((idx + 1) - len(values[idx]))]
    
    collected = 0

    for timestep in range(time):
        vals = [values[x + timestep][x] for x in (range(time - timestep))]
        collected += sorted(vals, reverse = True)[0]
        
    print(collected)