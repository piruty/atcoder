def execute(a, b, h):
    return (a + b) * h // 2


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    h = int(input())
    print(execute(a, b, h))
