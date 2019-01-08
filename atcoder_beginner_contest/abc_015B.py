import math


def execute(n, an):
    # an = list(filter(lambda a: a != 0, an))
    an = list(filter((0).__ne__, an))
    return math.ceil(sum(an) / len(an))


if __name__ == '__main__':
    n = int(input())
    an = list(map(int, input().split()))
    print(execute(n, an))

