# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc032/submissions/3494614

s, k = input(), int(input())
# {} = set
print(len({s[i:i+k] for i in range(len(s) - k + 1)}))
