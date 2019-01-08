def execute(s):
    r = ''
    for b in s:
        if b == 'B':
            r = r[0:-1]
        else:
            r += b
    return r


if __name__ == '__main__':
    print(execute(input()))
