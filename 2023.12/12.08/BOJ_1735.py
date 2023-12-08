import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

x_num, x_deno = map(int, input().split())
y_num, y_deno = map(int, input().split())

num = (x_num*y_deno) + (y_num*x_deno)
deno = x_deno * y_deno

_gcd = gcd(num, deno)

numerator = num // _gcd
denominator = deno // _gcd

print(numerator, denominator)