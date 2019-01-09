def execute(w):
    if len(w) % 2 == 1:
        return 'No'

    for i in range(len(w) // 2):
        if w.count(w[i]) % 2 == 1:
            return 'No'
    return 'Yes'


if __name__ == '__main__':
    print(execute(input()))
