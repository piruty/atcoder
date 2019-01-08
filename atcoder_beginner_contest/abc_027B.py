def execute(n, an):
    if sum(an) % n:
        return -1
    t = sum(an) // n
    b = 0
    for i in range(1, n):
        b += not (sum(an[:i]) == t * i and sum(an[i:]) == t * (n - i))
    return b


if __name__ == '__main__':
    n = int(input())
    an = list(map(int, input().split()))
    print(execute(n, an))
