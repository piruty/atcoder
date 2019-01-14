def execute(n, k):
    return k * (k - 1) ** (n - 1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(execute(n, k))
