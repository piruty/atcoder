def execute(n, k, x, y):
    return x * min(n, k) + y * max(0, n - k)


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    print(execute(n, k, x, y))
