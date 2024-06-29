# 치킨배달
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(m, ch):

    global min_v
    if m==len(chick):# 전체 치킨집 다 돌았을 때
        if len(ch) == M: # 최대 개수와 같다면
            city = 0
            # print(home, ch)
            for i in range(len(home)):
                hi, hj = home[i][0], home[i][1]
                h_dis = []
                for i in range(len(ch)):
                    ci, cj = ch[i][0], ch[i][1]
                    h_dis.append(abs(hi-ci)+abs(hj-cj))
                    # print(h_dis)
                city += min(h_dis)
            # print(city)
            min_v = min(min_v, city)
        return

    dfs(m+1, ch+[chick[m]]) # 유지
    dfs(m+1, ch) # 폐업

# M: 치킨집 최대 개수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = []
chick = [] # 치킨집 위치
home = [] # 집 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: # 치킨집이면
            chick.append((i,j))
        if arr[i][j] == 1: # 집이면
            home.append((i,j))

min_v = 20001
# print('chick: ', chick)
dfs(0, []) # 최대 치킨집 개수, 그 개수만큼 더하기
print(min_v)