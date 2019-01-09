# /usr/bin/env python
# coding: utf-8

# 複数入力を受け付けるのに [... for _ in [0] * n] はよく見るリスト内包表記
a = [int(input()) for i in [0] * 4]
print(min(a[:2]) * a[2] + max(0, a[0] - a[1]) * a[3])
