
data = list(map(int, input().split()))

n = data[0]
found = False

for x in data[1:n + 1]:
    if x == 0:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
