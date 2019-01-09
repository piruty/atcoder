# /usr/bin/env python
# coding: utf-8

w = input()
# all(): すべての要素がTrue（数値なら1）であればTrue、それ以外はFalseを返す（any()もある）
print("Yes" if all([w.count(x) % 2 == 0 for x in w]) else "No")
