# 가능한 많이 나누자
# 나누기가 1 빼는 것보다 빠르게 줄어듬 -> 최적의 해 보장
# 1을 계속 빼면 언젠간 1이 나옴 -> 최적의 해 보장

n,k = map(int, input().split())
answer=  0

while True:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
        answer += 1
    else:
        n = n - 1
        answer += 1

print(answer)