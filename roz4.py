a, b = (int(x) for x in input().split())
sum = 0
if a % 2 == 1:
    for i in range(a, b + 1, 2):
        sum += i
else:
    for i in range(a + 1, b + 1, 2):
        sum += i
print(sum)
