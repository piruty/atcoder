n = int(input())

tm = 100
for i in range(n):
    t = int(input())
    if t < tm:
        tm = t
print(tm)
