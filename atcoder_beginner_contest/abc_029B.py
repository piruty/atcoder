def execute(sn):
    return sum(map(lambda s: 'r' in s, sn))


if __name__ == '__main__':
    sn = []
    for _ in range(12):
        sn.append(input())
    print(execute(sn))
