n, k = map(int, input().split())
r = sorted(list(map(int, input().split())))[-1 * k:]

total = 0
for i in r:
    total = (total + i) / 2.0
print(total)


