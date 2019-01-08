def execute(n, q, lrtn):
    result = [0] * n
    for lrti in lrtn:
        result[lrti[0] - 1:lrti[1]] = [lrti[2]] * (lrti[1] - lrti[0] + 1)
    return '\n'.join(map(str, result))


if __name__ == '__main__':
    n, q = map(int, input().split())
    lrtn = []
    for _ in range(q):
        lrtn.append(list(map(int, input().split())))
    print(execute(n, q, lrtn))
