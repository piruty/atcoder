def execute(month):
    return int(month) % 12 + 1


if __name__ == '__main__':
    print(execute(input()))
