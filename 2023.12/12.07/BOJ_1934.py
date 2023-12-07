import sys

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a


def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result


N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(lcm(A, B))
