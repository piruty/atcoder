# https://beta.atcoder.jp/contests/abc025/submissions/3640493
n, a, b = map(int, input().split())
s = sum([1, -1][d > "East"] * [[int(e), b], [a]][a > int(e)] for d, e in [input().split() for _ in range(n)])
print([['', 'East '], ['West ', '']][0 > s][0 < s] + str(abs(s)))
