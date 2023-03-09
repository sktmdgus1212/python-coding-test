n, k = map(int, input().split(" "))

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

a.sort(reverse=True)
b.sort()

a_index = 0
b_index = n-1

for i in range(k):
    if a[-1] < b[-1]:
        a[n-1], b[n-1] = b[n-1], a[n-1]
    a.sort(reverse=True)
    b.sort()
print(sum(a))
