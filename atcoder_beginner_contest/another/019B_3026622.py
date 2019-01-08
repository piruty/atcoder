# https://beta.atcoder.jp/contests/abc019/submissions/3026622

from itertools import groupby

s = list(input())
ans = ''
for k, g in groupby(s):
    ans += k + str(len(list(g)))
print(ans)
