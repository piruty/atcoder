def execute(S):
    return '{} {} {} {} {} {}'.format(S.count('A'), S.count('B'), S.count('C'), S.count('D'), S.count('E'), S.count('F'))


if __name__ == '__main__':
    print(execute(input()))
