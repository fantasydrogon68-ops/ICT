summ = 0
flag = True
prev = ""
for i in range(10):
    a = int(input())
    summ += a
    if prev != "" and prev > a:
        flag = False
    prev = a
print(summ)
print(flag)
