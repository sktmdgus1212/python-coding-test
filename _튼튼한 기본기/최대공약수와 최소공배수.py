a, b = map(int, input().split(" "))

min_val = min(a, b)

ans1 = 1
ans2 = 1

for i in range(2, min_val+1):
    while a % i == 0 and b % i == 0:
        ans1 *= i
        ans2 *= i
        a = a // i
        b = b // i

ans2 = ans2 * a * b

print(ans1)
print(ans2)