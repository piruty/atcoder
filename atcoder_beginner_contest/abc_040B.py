def execute(n):
    w = n
    for i in range(1, n + 1):
        w = min(w, abs(n // i - i) + n % i)
        print(w)
    return w


if __name__ == '__main__':
    print(execute(int(input())))
