import sys

input = sys.stdin.readline

def fibonacci(n):
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    cnt = 0
    for i in range(3, N+1):
        cnt += 1
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[i], cnt

N = int(input())

code1, code2 = fibonacci(N)
print(code1, code2)
