def execute(a, b, c):
    return len({a, b, c})


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
