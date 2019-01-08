def execute(n):
    result = []
    for i in [8, 4, 2, 1]:
        if n < i:
            continue
        result.append(i)
        n = n % i
    result = result[::-1]
    result.insert(0, len(result))
    return result


if __name__ == '__main__':
    for i in execute(int(input())):
        print(i)
