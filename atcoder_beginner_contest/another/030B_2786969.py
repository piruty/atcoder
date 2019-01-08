# /usr/bin/env python
# coding: utf-8

d = 5.5 * eval(input().replace(' ', '* 60 + ')) % 360
print(min(d, 360 - d))
