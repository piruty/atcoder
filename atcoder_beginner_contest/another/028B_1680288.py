# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc028/submissions/1606137

S = input()
print(*[S.count(x) for x in 'ABCDEF'])
