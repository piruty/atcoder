def execute(h, w, c):
    result = []
    for ci in c:
        result.append(ci)
        result.append(ci)
    return result


if __name__ == '__main__':
    h, w = map(int, input().split())
    c = []
    for _ in range(h):
        c.append(input())
    for ci in execute(h, w, c):
        print(ci)
