from sys import stdin

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

if __name__ == '__main__':
    for line in stdin:
        n = []
        for w in line.strip().split():
            if w[0] in vowels:
                n.append(w + "yay")
            else:
                idx = 0
                for i, c in enumerate(w):
                    if c in vowels:
                        idx = i
                        break
                n.append(w[idx:] + w[:idx] + 'ay')
        print(' '.join(n))
