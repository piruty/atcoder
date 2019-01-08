def execute(a, b, c):
    result = 0
    if a + b == c:
        result += 1
    if a - b == c:
        result += 2

    return '!' if result == 0 \
        else '+' if result == 1 \
        else '-' if result == 2 \
        else '?'


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(execute(a, b, c))
