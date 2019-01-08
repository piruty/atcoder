import math


def execute(a, b):
    return math.ceil(b / a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(execute(a, b))
