def execute(s, n):
    n -= 1
    return s[int(n/5)] + s[n % 5]


if __name__ == '__main__':
    s = input()
    n = int(input())
    print(execute(s, n))
