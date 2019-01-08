# /usr/bin/env python
# coding: utf-8

a, b, n = [int(input()) for i in [0] * 3]
# nから始めて、aとbの両方で割り切れる数になるまで1つずつ大きくする
while n % a + n % b:
    n += 1
print(n)