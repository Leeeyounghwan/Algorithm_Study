import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

answer = 0

for i in combinations(card, 3):
    # combinations로 조합한 3개의 숫자 합이 answer보다 크고 M보다 작을 때,
    if answer < sum(i) and sum(i) <= M:
        answer = sum(i)

print(answer)
