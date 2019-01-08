def execute(m, d):
    return 'YES' if m % d == 0 else 'NO'


if __name__ == '__main__':
    m, d = map(int, input().split())
    print(execute(m, d))
