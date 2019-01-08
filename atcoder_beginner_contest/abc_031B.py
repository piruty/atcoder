def execute(l, h, n, an):
    result = []
    for ai in an:
        result.append("-1" if ai > h else "0" if ai >= l else str(l - ai))
    return '\n'.join(result)


if __name__ == '__main__':
    l, h = map(int, input().split())
    n = int(input())
    an = []
    for _ in range(n):
        an.append(int(input()))
    print(execute(l, h, n, an))
