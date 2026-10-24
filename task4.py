
x, d = input().split()
d = int(d)

count = 0

for digit in x:
    if int(digit) == d:
        count += 1

print(count)
