# /usr/bin/env python
# coding: utf-8

# https://atcoder.jp/contests/abc038/submissions/3566169
i = lambda: set(input().split())
print('YES' if i() & i() else 'NO')
