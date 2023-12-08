import sys

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(x, y):
    return (x * y) // gcd(x, y)


A, B = map(int, input().split())

print(lcm(A, B))
