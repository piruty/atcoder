def execute(s, t):
    l = abs(s.count('R') - s.count('L')) + abs(s.count('U') - s.count('D'))
    q = s.count('?')
    if t == 1:
        return l + q
    if l > q:
        return l - q
    return (q - l) % 2


if __name__ == '__main__':
    print(execute(input(), int(input())))
