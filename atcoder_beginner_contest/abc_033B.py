def execute(n, sp):
    t = 0
    m = 0
    s = ''
    for si, pi in sp:
        t += pi
        if pi > m:
            m = pi
            s = si
    return s if m > (t / 2) else 'atcoder'


if __name__ == '__main__':
    n = int(input())
    sp = []
    for _ in range(n):
        s, p = input().split()
        sp.append([s, int(p)])
    print(execute(n, sp))
