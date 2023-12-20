import sys

input = sys.stdin.readline

N = int(input())
li = []

for i in range(N):
    li.append(int(input()))

li.sort()

print(round(sum(li) / N))  # 산술평균
print(li[len(li) // 2])     # 중앙값

# 최빈값
dic = dict()
for i in li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(li) - min(li))    # 범위