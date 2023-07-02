arr = []

for i in range(9):
    arr.append(int(input()))

arr.sort()
sum_arr = sum(arr)
a, b= 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if sum_arr - arr[i] - arr[j] == 100:
            a = i
            b = j   

for i in range(9):
    if i == a or i == b:
        continue
    print(arr[i])