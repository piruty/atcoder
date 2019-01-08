#! /usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

count = 0
while True:
    for i in range(n):
        if a[i] % 2 == 1:
            print(count)
            exit()
        a[i] /= 2
    count += 1
