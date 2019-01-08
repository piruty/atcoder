def execute(value):
    n = int(value)

    h = int(n / 3600)
    m = int((n - 3600 * h) / 60)
    s = n - 3600 * h - 60 * m

    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


if __name__ == '__main__':
    print(execute(input()))
