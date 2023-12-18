import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


qs = list(map(int, input().split()))
numbers = list(map(int, input().split()))

M = int(input())
m_numbers = list(map(int, input().split()))

answer = deque()

for i in range(N):
    if qs[i] == 0:
        answer.appendleft(numbers[i])

for j in range(M):
    answer.append(m_numbers[j])
    print(answer.popleft(), end=' ')