n = int(input())

total = 0
for a in map(int, input().split()):
    a -= 1
    if a % 6 == 0 or (a - 2) % 6 == 0:
        continue
    if (a - 1) % 6 == 0:
        total += 1
        continue
    total += (a % 3) + 1
print(total)


