def execute(a, b, c):
    s = sorted([a, b, c])[::-1]
    return [s.index(a) + 1, s.index(b) + 1, s.index(c) + 1]


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    result = execute(a, b, c)

    for r in result:
        print(r)
