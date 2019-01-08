def execute(n, x):
    return min(n - x, x - 1)


if __name__ == '__main__':
    n, x = map(int, input().split())
    print(execute(n, x))
