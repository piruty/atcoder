n = int(input())

m = 0
prices = set()
for i in range(n):
    a = int(input())
    if a > m:
        m = a
    prices.add(a)

prices.remove(m)
print(max(prices))

