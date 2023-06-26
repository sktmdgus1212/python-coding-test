tc = int(input())
for i in range(tc):
    n = int(input())
    count = 0
    arr = []
    while n > 0:
        remainder = n % 2

        if remainder == 1:
            arr.append(count)
        count += 1
        n = n // 2

    for a in arr:
        print(a, end=" ")