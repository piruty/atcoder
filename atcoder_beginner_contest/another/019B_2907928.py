# https://beta.atcoder.jp/contests/abc019/submissions/2907928

s = list(input())
t = ''
while s:
    head = s.pop(0)
    count = 1
    while s and s[0] == head:
        del s[0]
        count += 1
    t += head + str(count)
print(t)
