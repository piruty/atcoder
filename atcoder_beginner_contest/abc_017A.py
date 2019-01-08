def execute(se):
    score = 0
    for s, e in se:
        score += s * e // 10
    return score


if __name__ == '__main__':
    se = []
    for i in range(3):
        se.append(list(map(int, input().split())))
    print(execute(se))
