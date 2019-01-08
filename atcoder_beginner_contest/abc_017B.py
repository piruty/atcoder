def execute(x):
    return 'YES' if x.replace('ch', '').replace('o', '').replace('k', '').replace('u', '') == '' else 'NO'


if __name__ == '__main__':
    print(execute(input()))
