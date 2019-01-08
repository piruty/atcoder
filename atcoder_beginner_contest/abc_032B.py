def execute(s, k):
    if len(s) < k:
        return 0
    p = []
    for i in range(0, len(s) - k + 1):
        p.append(s[i:i+k])
    return len(set(p))


if __name__ == '__main__':
    s = input()
    k = int(input())
    print(execute(s, k))
