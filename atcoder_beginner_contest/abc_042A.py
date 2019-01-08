def execute(s):
    return ['NO', 'YES'][s.count('5') == 2 and s.count('7') == 1]


if __name__ == '__main__':
    print(execute(input()))
