def execute(n, a, b, sdi):
    position = 0
    for s, d in sdi:
        d = int(d)
        d = a if d < a else b if d > b else d
        position += d * (1 if s == 'East' else -1)
    if position == 0:
        return '0'
    return '{} {}'.format('East' if position > 0 else 'West', abs(position))


if __name__ == '__main__':
    n, a, b = map(int, input().split())
    sdi = []
    for _ in range(n):
        sdi.append(list(input().split()))
    print(execute(n, a, b, sdi))
