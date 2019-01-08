# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc017/submissions/3106925
print(sum(eval(input().replace(' ', '*')) for _ in [0] * 3) // 10)