def execute(a, b):
    return a if len(a) > len(b) else b


if __name__ == '__main__':
    print(execute(input(), input()))

