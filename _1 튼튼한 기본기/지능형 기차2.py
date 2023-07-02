current = 0
max_total = 0
for i in range(10):
    down, up = map(int, input().split(" "))
    
    current -= down
    current += up
    if max_total < current:
        max_total = current
print(max_total)