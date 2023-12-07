import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

num_dict = {}

for number in numbers:
    if number in num_dict:
        num_dict[number] += 1
    else:
        num_dict[number] = 1


for check in check:
    if check in num_dict:
        print(num_dict[check], end=" ")
    else:
        print(0, end=" ")