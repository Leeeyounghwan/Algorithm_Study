import sys

input = sys.stdin.readline

N = int(input())

prime = [True for _ in range(1000001)]

# 에라토스테네스의 체로 소수 판별하기
for i in range(2, 1001):
    if prime[i]:
        for j in range(i + i, 1000001, i):
            prime[j] = False

for _ in range(N):
    number = int(input())
    cnt = 0

    for i in range(2, number // 2 + 1):
        # print(i, number - i, prime[i], prime[number - i])
        if prime[i] and prime[number - i]:
            cnt += 1
    print(cnt)
