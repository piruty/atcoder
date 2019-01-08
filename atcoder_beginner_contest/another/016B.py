# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc016/submissions/3317764
a, b, c = map(int, input().split())
print('!+-?'[(a + b == c) + 2 * (a - b == c)])
