def execute(A, B, C, K, S, T):
    return A * S + B * T - (C * (S + T) if S + T >= K else 0)


if __name__ == '__main__':
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())
    print(execute(A, B, C, K, S, T))
