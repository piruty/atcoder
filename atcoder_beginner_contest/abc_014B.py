def execute(X, an):
    binx = bin(X)[2:]
    total = 0
    for i, b in enumerate(binx[::-1]):
        if b == '1':
            total += an[i]
    return total


if __name__ == '__main__':
    n, X = map(int, input().split())
    an = list(map(int, input().split()))
    print(execute(X, an))

