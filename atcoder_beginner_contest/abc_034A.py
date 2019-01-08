def execute(x, y):
    return ["Worse", "Better"][x < y]


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(execute(x, y))
