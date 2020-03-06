def test_num(_1, _2, _3, _4, _5):
    if (_1 == '***' and _2 == '* *' and _3 == '* *' and _4 == '* *' and _5 == '***'):
        return '0'
    elif (_1 == '  *' and _2 == '  *' and _3 == '  *' and _4 == '  *' and _5 == '  *'):
        return '1'
    elif (_1 == '***' and _2 == '  *' and _3 == '***' and _4 == '*  ' and _5 == '***'):
        return '2'
    elif (_1 == '***' and _2 == '  *' and _3 == '***' and _4 == '  *' and _5 == '***'):
        return '3'
    elif (_1 == '* *' and _2 == '* *' and _3 == '***' and _4 == '  *' and _5 == '  *'):
        return '4'
    elif (_1 == '***' and _2 == '*  ' and _3 == '***' and _4 == '  *' and _5 == '***'):
        return '5'
    elif (_1 == '***' and _2 == '*  ' and _3 == '***' and _4 == '* *' and _5 == '***'):
        return '6'
    elif (_1 == '***' and _2 == '  *' and _3 == '  *' and _4 == '  *' and _5 == '  *'):
        return '7'
    elif (_1 == '***' and _2 == '* *' and _3 == '***' and _4 == '* *' and _5 == '***'):
        return '8'
    elif (_1 == '***' and _2 == '* *' and _3 == '***' and _4 == '  *' and _5 == '***'):
        return '9'
    else:
        return 'undefined'

if __name__ == '__main__':
    _1 = input()
    _2 = input()
    _3 = input()
    _4 = input()
    _5 = input()
    numbers = []
    for i in range(int(len(_1)/4) + 1):
        num = test_num(_1[i*4:(i*4 + 3)], _2[i*4:(i*4 + 3)], _3[i*4:(i*4 + 3)], _4[i*4:(i*4 + 3)], _5[i*4:(i*4 + 3)])
        numbers.append(num)

    if 'undefined' in numbers:
        print("BOOM!!")
    elif int(''.join(numbers)) % 6 != 0:
        print('BOOM!!')
    else:
        print("BEER!!")

        

