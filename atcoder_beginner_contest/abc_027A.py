def execute(ln):
    ln = sorted(ln)
    return ln[2] if ln[0] == ln[1] else ln[0]


if __name__ == '__main__':
    print(execute(list(map(int, input().split()))))
