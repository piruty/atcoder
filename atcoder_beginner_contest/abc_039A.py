def execute(a, b, c):
    return 2 * (a * b + a * c + b * c)


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
