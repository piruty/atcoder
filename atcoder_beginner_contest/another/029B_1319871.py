# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc029/submissions/1319871
# 'rrrrrrrrrrrr' の1文字ずつに対してループを回している
print(sum(x in input() for x in 'r' * 12))
