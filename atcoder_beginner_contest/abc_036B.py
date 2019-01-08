def execute(n, snn):
    r = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            r[j][n - i - 1] = snn[i][j]
    return '\n'.join(''.join(row) for row in r)


if __name__ == '__main__':
    n = int(input())
    snn = []
    for _ in range(n):
        snn.append(list(input()))
    print(execute(n, snn))
