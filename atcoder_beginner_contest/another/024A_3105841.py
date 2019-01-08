# https://beta.atcoder.jp/contests/abc024/submissions/3105841
i = lambda: map(int, input().split())
a, b, c, k = i()
s, t = i()
print(a * s + b * t - (c * (s + t)) * (s + t >= k))
