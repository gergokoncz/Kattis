def calc(p, den, nom):
    n =  nom * p + den
    d = nom
    return n, d

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    den = 1
    nom = a[n-1]
    while (n - 2) >= 0:
#        print(nom, den)
        nom, den = calc(a[n-2], den, nom)
        n -= 1
    print('{}/{}'.format(nom, den))

