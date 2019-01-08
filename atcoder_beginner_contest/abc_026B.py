import math


def execute(n, rn):
    rn = sorted(rn)[::-1]
    return (sum([x**2 for x in rn[::2]]) - sum([x**2 for x in rn[1::2]])) * math.pi


if __name__ == '__main__':
    n = int(input())
    rn = []
    for _ in range(n):
        rn.append(int(input()))
    print(execute(n, rn))
