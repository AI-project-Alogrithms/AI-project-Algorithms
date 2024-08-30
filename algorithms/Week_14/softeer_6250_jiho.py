# 성적 평가
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def each_score(lst):
    ans_lst = [0 for _ in range(n)]
    cur = 1
    for idx, (ori_idx, score) in enumerate(lst):
        if idx>0 and lst[idx][1] == lst[idx-1][1]: # 같은 등수라면
            ans_lst[ori_idx] = cur
        else:
            cur = idx+1 # 등수 업데이트
            ans_lst[ori_idx] = cur

    print(" ".join(map(str, ans_lst)))

n = int(input())
total = [0 for _ in range(n)]
test = [list(map(int, input().split())) for _ in range(3)]
for t in test:
    lst = []
    for idx, score in enumerate(t):
        lst.append((idx, score))
        total[idx]+=score # 최종 스코어 뽑기
    lst.sort(key=lambda x: x[1], reverse=True)

    each_score(lst)

total_lst = []
for idx, score in enumerate(total):
    total_lst.append((idx, score))
total_lst.sort(key=lambda x: x[1], reverse=True)
each_score(total_lst)

