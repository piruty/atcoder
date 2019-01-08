def execute(N, a, b, K, P):
    P.extend([a, b])
    return 'YES' if K + 2 == len(set(P)) else 'NO'


if __name__ == '__main__':
    N = int(input())
    a, b = map(int, input().split())
    K = int(input())
    P = list(map(int, input().split()))
    print(execute(N, a, b, K, P))
