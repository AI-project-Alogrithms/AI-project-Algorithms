import sys
input=sys.stdin.readline

from collections import defaultdict

N = int(input())
data = []

for i in range(N):
    age, name = input().split()
    data.append([int(age), i, name]) # int 안해주면 오류나는데, 이유는 정확히 모르겠음

sorted_list = sorted(data, key=lambda x:(x[0], x[1]))

for data in sorted_list:
    print(data[0], data[2])