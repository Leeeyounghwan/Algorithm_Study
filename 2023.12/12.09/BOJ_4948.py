import sys
from math import sqrt

input = sys.stdin.readline

length = 123456 * 2 + 1
isPrime = [1] * length

for i in range(1, length):
    if i == 1:
        continue
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            isPrime[i] = 0
            break

while True:
    N = int(input())
    cnt = 0
    if N == 0:
        break

    else:
        for i in range(N + 1, N * 2 + 1):
            cnt += isPrime[i]
        print(cnt)