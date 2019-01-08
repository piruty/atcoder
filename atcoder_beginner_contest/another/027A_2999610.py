# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc027/submissions/2999610
a, b, c = sorted(map(int, input().split()))
print([a, c][a == b])