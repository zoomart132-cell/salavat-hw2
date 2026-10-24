
data = list(map(int, input().split()))

n = data[0]
zeros = 0
positive = 0
negative = 0

for x in data[1:n + 1]:
    if x == 0:
        zeros += 1
    elif x > 0:
        positive += 1
    else:
        negative += 1

print(zeros, positive, negative)
