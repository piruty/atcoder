def execute(a, b, n):
    h = max(a, b)
    m = min(a, b)
    i = 1
    while True:
        if m * i >= n and (m * i) % h == 0:
            return m * i
        i += 1


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    n = int(input())
    print(execute(a, b, n))
