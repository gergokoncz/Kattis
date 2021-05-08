def is_valid(m):
    if len(m) < 5:
        return False
    if len(m) != len(set(m)):
        return False
    return True

if __name__ == '__main__':
    names = [input().strip() for _ in range(int(input()))]
    valid_names = list(filter(is_valid, names))
    if len(valid_names) > 0:
        min_l = min(map(len, valid_names)) 
        print(sorted([n for n in valid_names if len(n) == min_l])[-1])
    else:
        print('neibb!')