def execute(a, op, b):
    return eval(a + op + b)


if __name__ == '__main__':
    a, op, b = input().split()
    print(execute(a, op, b))
