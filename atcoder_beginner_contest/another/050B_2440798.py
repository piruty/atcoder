# /usr/bin/env python
# coding: utf-8

input()
*a, = map(int, input().split())
for _ in [0] * int(input()):
    i, x = map(int, input().split())
    print(sum(a) - a[~-i] + x)
