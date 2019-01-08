#! /usr/bin/env python3

n, t = map(int, input().split())

for x in range(n+1):
    for y in range(n+1-x):
        z = n - x - y
        if 10000 * x + 5000 * y + 1000 * z == t:
            print('{} {} {}'.format(x, y, z))
            exit()
print('-1 -1 -1')

#x, y, x = 0, 0, 0
#
#x = int(t / 10000)
#if x > n:
#    print("-1 -1 -1")
#    exit()
#
#t = t % 10000
#y = int((t / 5000))
#if (x + y) > n:
#    print("-1 -1 -1")
#    exit()
#
#t = t % 5000
#z = int((t / 1000))
#if (x + y + z) > n:
#    print("-1 -1 -1")
#    exit()
#
#print("{} {} {}".format(x, y, z))
