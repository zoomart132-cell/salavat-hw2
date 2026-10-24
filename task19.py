
n = int(input())

count = 0
i = 1

while count < n:
    for j in range(i):
        if count < n:
            print(i, end=" ")
            count += 1
    i += 1
