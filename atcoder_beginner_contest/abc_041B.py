def execute(a, b, c):
    return (a * b * c) % (10**9 + 7)


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
