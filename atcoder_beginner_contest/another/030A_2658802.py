# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc030/submissions/2658802
A, B, C, D = map(int, input().split())
print(["TAKAHASHI", "AOKI", "DRAW"][(B / A <= D / C) * (B / A == D / C)])
