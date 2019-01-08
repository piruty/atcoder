def execute(n, l, sn):
    return ''.join(sorted(sn))


if __name__ == '__main__':
    n, l = map(int, input().split())
    sn = []
    for _ in range(n):
        sn.append(input())
    print(execute(n, l, sn))
