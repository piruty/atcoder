def execute(a, d):
    return max((a + 1) * d, a * (d + 1))


if __name__ == '__main__':
    a, d = map(int, input().split())
    print(execute(a, d))
