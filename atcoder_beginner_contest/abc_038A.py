def execute(S):
    return ['NO', 'YES'][S[-1] == 'T']


if __name__ == '__main__':
    print(execute(input()))
