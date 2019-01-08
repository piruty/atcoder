def execute(x):
    # return int(pow(x, .25))
    for n in range(10**9):
        if n**4 == x:
            return n


if __name__ == '__main__':
    print(execute(int(input())))
