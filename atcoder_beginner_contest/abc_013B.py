def execute(a, b):
    if abs(a - b) > 5:
        if a > b:
            b += 10
        else:
            a += 10
    return abs(a - b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(execute(a, b))
