def execute(w, h):
    return ['4:3', "16:9"][w % 16 == 0 and h % 9 == 0]


if __name__ == '__main__':
    w, h = map(int, input().split())
    print(execute(w, h))
