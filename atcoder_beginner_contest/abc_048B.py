def execute(a, b, x):
    if a == b:
        return 0
    count = (b - a) // x
    if a == 0:
        count += 1
    if x % 2 == 0:
        count += 1
    return count


if __name__ == '__main__':
    a, b, x = map(int, input().split())
    print(execute(a, b, x))
