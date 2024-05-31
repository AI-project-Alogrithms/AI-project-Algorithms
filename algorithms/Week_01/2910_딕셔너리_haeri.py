import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

from collections import defaultdict

N, C = map(int, input().split())
lst = list(input().split())

index_dict = {} # index 저장 딕셔너리
count_dict = defaultdict(int) # 빈도 수 저장 딕셔너리

for i, data in enumerate(lst): # 인덱스 표현을 위해 enumerate 이용 
    if data not in index_dict:
        index_dict[data] = i
    count_dict[data] += 1

print(' '.join(sorted(lst, key=lambda x:(-count_dict[x],index_dict[x])))) # 빈도수가 큰 순, 인덱스가 낮은 순에 따른 정렬