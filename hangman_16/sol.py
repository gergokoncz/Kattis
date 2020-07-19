if __name__ == '__main__':
    w = input().strip()
    wl = len(w)
    g = input().strip()
    e = 0
    for l in g:
        if l in w:
            wl -= w.count(l)
            if wl == 0:
                print("WIN")
                break
        else:
            e += 1
            if e == 10:
                print("LOSE")
                break
