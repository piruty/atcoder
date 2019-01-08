#! /usr/bin/env python3

n, a, b = map(int, input().split())

s = set()
if n == 10000:
    s.add(10000)
for s0 in range(10):
    for s1 in range(10):
        for s2 in range(10):
            for s3 in range(10):
                st = s0 + s1 + s2 + s3
                total = 1000 * s3 + 100 * s2 + 10 * s1 + s0
                if total > n or st < a or st > b:
                    continue
                s.add(total)
print(sum(s))
