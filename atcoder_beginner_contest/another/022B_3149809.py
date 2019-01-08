# https://beta.atcoder.jp/contests/abc022/submissions/3149809

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

ans = sum([v - 1 for k, v in Counter(A).items() if v >= 2])
