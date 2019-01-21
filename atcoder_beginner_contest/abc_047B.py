def execute(w, h, n, xya):
    s = [[1 for _ in range(w)] for _ in range(h)]
    for x, y, a in xya:
        for xi in range(w):
            for yi in range(h):
                if a == 1:
                    if xi < x:
                        s[yi][xi] = 0
                if a == 2:
                    if xi >= x:
                        s[yi][xi] = 0
                if a == 3:
                    if yi < y:
                        s[yi][xi] = 0
                if a == 4:
                    if yi >= y:
                        s[yi][xi] = 0
    return sum(map(sum, s))


if __name__ == '__main__':
    w, h, n = map(int, input().split())
    xya = []
    for _ in range(n):
        xya.append(list(map(int, input().split())))
    print(execute(w, h, n, xya))
