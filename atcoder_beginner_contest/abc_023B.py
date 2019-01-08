def execute(N, S):
    if len(S.replace('a', '').replace('b', '').replace('c', '')) != 0:
        return -1
    if len(S) % 2 != 1 or S[int(len(S)/2)] != 'b':
        return -1
    if S == 'b':
        return 0
    s = 'b'
    for n in range(N):
        n += 1
        if n % 3 == 0:
            s = 'b' + s + 'b'
        elif n % 3 == 1:
            s = 'a' + s + 'c'
        else:
            s = 'c' + s + 'a'
        if s == S:
            return n
    return -1



if __name__ == '__main__':
    print(execute(int(input()), input()))
