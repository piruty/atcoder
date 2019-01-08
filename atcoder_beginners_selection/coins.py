#! /usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
t = int(input())

count = 0

for i in range(int(t / 500) + 1):
    if i > a:
        break
    s = t - 500 * i
    if s == 0:
        count += 1
        continue
    for j in range(int(s / 100) + 1):
        if j > b:
            break
        s2 = s - 100 * j
        if s2 == 0:
            count += 1
            continue
        for k in range(int(s2 / 50) + 1):
            if k > c:
                break
            if (s2 - 50 * k) == 0:
                count += 1
print(count)
