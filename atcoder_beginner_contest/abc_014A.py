def execute(a, b):
    if a == b:
        return 0
    return b - a % b


if __name__ == '__main__':
    print(execute(int(input()), int(input())))

