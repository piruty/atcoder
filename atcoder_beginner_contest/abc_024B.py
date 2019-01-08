def execute(N, T, Ai):
    total = 0
    for i in range(1, N):
        total += max(min(T, Ai[i] - Ai[i - 1]), 0)
    return total + T


if __name__ == '__main__':
    N, T = map(int, input().split())
    Ai = [int(input()) for _ in range(N)]
    print(execute(N, T, Ai))
