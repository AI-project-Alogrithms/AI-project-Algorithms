import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

from collections import defaultdict

temp_list = list(input().split())
N = int(temp_list[0])
N -= (len(temp_list)-1)

all_list = temp_list[1:] # 데이터 개수(N) 제외한 나머지 데이터

for _ in range(N): # N개가 될 때까지 데이터 추가
    now_list = (list(input().split()))
    all_list.extend(now_list)
    N -= len(now_list)
    if N == 0:
        break

reverse_list = [int(x[::-1]) for x in all_list] # 각 문자열을 역순서로 정렬
for data in sorted(reverse_list): # 오름차순 정렬
    print(data)