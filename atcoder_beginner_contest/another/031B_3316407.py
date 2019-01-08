# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc031/submissions/3316407

l, h = map(int, input().split())
for _ in range(int(input())):
    t = int(input())
    print(max(l-t, 0) if h >= t else -1)
