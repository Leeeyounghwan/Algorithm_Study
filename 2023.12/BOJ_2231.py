import sys

input = sys.stdin.readline

N = int(input())  # 입력받은 분해합 저장

for i in range(1, N + 1):  # 입력받은 분해합의 생성자 찾기
    sum_digit = sum(map(int, str(i)))  # i의 각 자릿수를 더함
    sum_i = i + sum_digit  # 분해합 = 생성자 + 생성자 각 자릿수의 합

    if sum_i == N:
        print(i)
        break

    if i == N:  # 범위안에 생성자가 없을 때,
        print(0)
