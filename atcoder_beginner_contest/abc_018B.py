def execute(s, lr):
    for l, r in lr:
        l -= 1
        r -= 1
        s = s[:l] + s[l:r + 1][::-1] + s[r + 1:]
    return s


if __name__ == '__main__':
    s = input()
    n = int(input())
    lr = []
    for _ in range(n):
        lr.append(map(int, input().split()))
    print(execute(s, lr))
