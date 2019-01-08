def execute(a, b, c, d):
    r = b / a - d / c
    return 'TAKAHASHI' if r > 0 else 'AOKI' if r < 0 else 'DRAW'


if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    print(execute(a, b, c, d))
