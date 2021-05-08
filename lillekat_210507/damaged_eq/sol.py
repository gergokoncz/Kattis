if __name__ == '__main__':
    a, b, c, d = input().strip().split()
    ops = ['*', '+', '-', '//']
    count = 0
    for op1 in ops:
        for op2 in ops:
            try:
                if eval(a + op1 + b) == eval(c + op2 + d):
                    count += 1
                    print(f"{a} {'/' if op1 == '//' else op1} {b} = {c} {'/' if op2 == '//' else op2} {d}")
            except:
                None
    
    if count == 0:
        print('problems ahead')