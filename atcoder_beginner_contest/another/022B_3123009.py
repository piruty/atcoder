# https://beta.atcoder.jp/contests/abc022/submissions/3123009
N = int(input())
print(N - len(set([input() for _ in [0] * N])))
