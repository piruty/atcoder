def execute(N, S, T, WA):
    WB = 0
    count = 0
    for a in WA:
        WB += a
        if S <= WB <= T:
            count += 1
    return count


if __name__ == '__main__':
    N, S, T = map(int, input().split())
    WA = [int(input()) for _ in range(N)]

    print(execute(N, S, T, WA))
