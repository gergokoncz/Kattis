import math

def med(arr, s):
    if s % 2 == 1:
        return arr[int((s - 1) / 2)]
    else:
        return math.floor((arr[int(s / 2)] + arr[int(s / 2 - 1)]) / 2)

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(raw_input())
        arr = list(map(int, raw_input().split()))
        
        sum = arr[0]
        b_arr = [arr[0]]
        for el in arr[1:]:
            is_last = True
            for idx, ex in enumerate(b_arr):
                if el <= ex:
                    b_arr[idx + 1:] = b_arr[idx:]
                    b_arr[idx] = el
                    is_last = False
                    break
            if is_last:
                b_arr.append(el)
            sum += med(b_arr, len(b_arr))
        print(int(sum))
