
a, b = map(int, input().split())

for i in range(a, b + 1):
    if i >= 0 and int(i ** 0.5) ** 2 == i:
        print(i, end=" ")
