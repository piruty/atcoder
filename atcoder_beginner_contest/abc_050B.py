def execute(n, tn, m, pxm):
    result = []
    for px in pxm:
        cp = tn[:]
        cp[px[0] - 1] = px[1]
        result.append(sum(cp))
    return result


if __name__ == '__main__':
    n = int(input())
    tn = list(map(int, input().split()))
    m = int(input())
    pxm = []
    for _ in range(m):
        p, x = map(int, input().split())
        pxm.append([p, x])
    result = execute(n, tn, m, pxm)
    print("\n".join(map(str, result)))
