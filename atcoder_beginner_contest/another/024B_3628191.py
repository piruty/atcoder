# https://beta.atcoder.jp/contests/abc024/submissions/3628191
import sys

n, t = map(int, input().split())
count = 0
time = int(sys.stdin.readline())
for i in range(1, n):
    a = int(sys.stdin.readline())
    if time + t >= a:
        count += a - time
        time = a
    else:
        count += t
        time = a
print(count + t)
