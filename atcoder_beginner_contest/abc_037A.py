def execute(a, b, c):
    return c // min(a, b)


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
