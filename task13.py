
data = list(map(int, input().split()))

n = data[0]
count = 0

for x in data[1:n + 1]:
    if x == 0:
        count += 1

print(count)
