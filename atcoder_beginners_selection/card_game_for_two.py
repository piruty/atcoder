#! /usr/bin/env python3

n = int(input())
l = sorted(map(int, input().split()))

a = sum([x for x in l[-1::-2]])
b = sum([x for x in l[-2::-2]])
print(a-b)
