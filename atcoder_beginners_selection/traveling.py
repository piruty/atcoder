#! /usr/bin/env python3

n = int(input())
lt, lx, ly = 0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    dt = t - lt
    dx = x - lx
    dy = y - ly
    if abs(dx) + abs(dy) > dt:
        print('No')
        exit()
    if (dx+dy-dt) % 2 == 1:
        print('No')
        exit()
    lt = t
    lx = x
    ly = y
print('Yes')
