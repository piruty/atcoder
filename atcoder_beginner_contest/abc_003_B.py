s = input()
t = input()

for i in range(len(s)):
    ss = s[i]
    tt = t[i]
    if ss == '@':
        if tt in 'atcoder':
            continue
        print('You will lose')
        exit()
    elif tt == '@':
        if ss in 'atcoder':
            continue
        print('You will lose')
        exit()
    elif tt != ss:
        print('You will lose')
        exit()

print('You can win')
