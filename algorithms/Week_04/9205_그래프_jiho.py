# 맥주 마시면서 걸어가기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(hi, hj, fi, fj):
    q = deque()
    v = [0] * n  # 편의점 중복 확인
    q.append((hi,hj)) # 집은 방문에 표시 안함

    while (q):
        ci, cj = q.popleft()
        if (abs(ci - fi) + abs(cj - fj)<=1000):
            return 'happy'
        for i in range(n):
            if v[i] == 0: # 미방문
                ni, nj = p[i] # 편의점 좌표 꺼내기
                if (abs(ci - ni) + abs(cj - nj)<=1000):  # 범위 내
                    q.append((ni, nj))
                    v[i] = 1
    return 'sad'



case = int(input())
for _ in range(case):
    n = int(input()) # 편의점 개수
    p = []
    hi, hj = map(int, input().split()) # 집 좌표
    for _ in range(n): # 편의점 좌표
        pi, pj = map(int, input().split())
        p.append((pi, pj))

    fi, fj = map(int, input().split()) # 페스티벌 좌표
    # 하나하나의 편의점을 좌표로 저장하고 꺼내서 확인하기
    # 한번에 1000m 이동 가능, 현재 위치 기준으로(ci, cj), n개의 편의점 좌 표를 하나씩 1000m 이내인지 확인하기
    ans = bfs(hi, hj, fi, fj)
    print(ans)



