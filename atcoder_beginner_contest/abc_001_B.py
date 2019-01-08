m = int(input())

if m < 100:
    print('00')
elif m <= 5000:
    print('{:02}'.format(int(m / 100)))
elif m <= 30000:
    print('{}'.format(int(m / 1000) + 50))
elif m <= 70000:
    print('{}'.format(80 + int((m / 1000 - 30) / 5)))
else:
    print('89')

