def execute(s):
    w = 'a'
    while True:
        if len(s[w]) == 0:
            return w.upper()
        t = s[w][0]
        s[w] = s[w][1:]
        w = t


if __name__ == '__main__':
    s = {}
    s['a'] = input()
    s['b'] = input()
    s['c'] = input()
    print(execute(s))
