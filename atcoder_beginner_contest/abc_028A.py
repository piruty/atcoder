def execute(n):
    return 'Perfect' if n == 100 else 'Great'  if n >= 90 else 'Good' if n >= 60 else 'Bad'


if __name__ == '__main__':
    print(execute(int(input())))
