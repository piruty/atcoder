def execute(a, b, c):
    return sorted([a, b, c])[1]


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
