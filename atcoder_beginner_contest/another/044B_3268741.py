# /usr/bin/env python
# coding: utf-8

w = input()
# 文字ごとに2で割り切れる数が含まれているか検証し、
# 全て0（2で割り切れる）ならsumが0になり"YNeos"[0::2](= Yes)となる
# 一つでも割り切れないものがあれば、"YNeos"[1::2](= No)
print("YNeos"[sum(w.count(c) % 2 for c in w) > 0::2])
