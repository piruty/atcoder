def execute(a, b, c):
    s = sorted([a, b, c])
    return 'YNeos'[s[2] != (s[0] + s[1])::2]


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
