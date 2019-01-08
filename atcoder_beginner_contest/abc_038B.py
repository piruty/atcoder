def execute(hw1, hw2):
    return ['NO', 'YES'][max((i in hw2) for i in hw1)]


if __name__ == '__main__':
    hw1 = list(map(int, input().split()))
    hw2 = list(map(int, input().split()))
    print(execute(hw1, hw2))
