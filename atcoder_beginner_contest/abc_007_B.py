n = input()
if n == 'a':
    print(-1)
else:
    if len(n) == 1:
        print('a')
    else:
        print('a' * (len(n) - 1))
