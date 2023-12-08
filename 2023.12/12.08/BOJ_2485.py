import sys

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N = int(input())

li = []
dist = []

for i in range(N):
    li.append(int(input().rstrip()))
    if i != 0:
        dist.append(li[i] - li[i - 1])

max_gcd = dist[0]

for j in range(1, len(dist)):
    max_gcd = gcd(max_gcd, dist[j])


result = 0
for item in dist:
    result += item // max_gcd - 1
print(result)
