def execute(n, m):
    h = ((n % 12) * 60 + m) * 0.5
    m = m * 6
    d = abs(h - m)
    return min(d, 360 - d)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(execute(n, m))
