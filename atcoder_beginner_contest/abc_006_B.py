n = int(input())
a1 = 0
a2 = 0
a3 = 1

if n == 1 or n == 2:
    print(0)
    exit()

if n == 3:
    print(1)
    exit()

a = 0
for i in range(3, n):
    a = a1 + a2 + a3
    a1, a2, a3 = a2, a3, a
    if a1 > 10007:
        a1 %= 10007
        a2 %= 10007
        a3 %= 10007
print(a % 10007)
