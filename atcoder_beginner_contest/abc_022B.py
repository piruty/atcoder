def execute(A):
    count = 0
    setA = set([])
    for a in A:
        if a in setA:
            count += 1
        setA.add(a)
    return count


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(execute(A))
