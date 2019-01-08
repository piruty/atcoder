def execute(a, b):
    return str(int(a + b) * 2)


if __name__ == '__main__':
    a, b = input().split()
    print(execute(a, b))
