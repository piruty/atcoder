def execute(n):
    return 'SAME' if len(set(list(n))) == 1 else 'DIFFERENT'
    pass


if __name__ == '__main__':
    print(execute(input()))
