# 시간 복잡도 log

n,k = map(int, input().split())
answer=  0

while True:
    # 나눌 수 있을 때까지 1 빼기
    target = (n // k) * k
    answer += (n - target)
    n = target

    # 더 이상 나눌 수 없으면 탈출
    if n < k:
        break

    # 나누기 연산
    answer += 1
    n //= k

answer += (n-1)
print(answer)