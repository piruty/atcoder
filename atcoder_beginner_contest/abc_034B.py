def execute(n):
    return n + [-1, 1][n % 2 == 1]


if __name__ == '__main__':
    print(execute(int(input())))
