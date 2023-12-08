import sys, math

input = sys.stdin.readline

N = int(input())


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for _ in range(N):
    number = int(input())
    while True:
        if number == 0 or number == 1:
            print(2)
            break
        if isPrime(number):
            print(number)
            break
        else:
            number += 1
