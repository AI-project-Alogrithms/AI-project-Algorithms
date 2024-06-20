import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt")
input = sys.stdin.readline


def cal(ch, home):
    ans = 0 # 거리 중 최소 값 누적
    # 각 집마다 치킨 집 거리
    for i in range(len(home)):
        hi, hj = home[i][0], home[i][1]
        h = [] # 현재 집 위치에서 치킨 집 까지의 거리 넣기
        for i in range(len(ch)):
            ci, cj = ch[i][0], ch[i][1]
            h.append(abs(hi-ci)+abs(hj-cj))
        # print(h)
        ans += min(h)
        # print("ans: ", ans)
    return ans

def dfs(n, tlst):
    global total
    if n == cnt: # 치킨집 개수가 전체 치킨집 개수만큼 갔다면 (각 치킨집마다 선택하기/안하기)
        if len(tlst) == m: # 치킨집 개수가 m과 동일하면
            total = min(total, cal(tlst, home))
        return
    # 하부 함수 호출
    dfs(n+1, tlst+[ch[n]]) # 유지하는 경우
    dfs(n+1, tlst) # 폐업하는 경우


n, m = map(int, input().split())
arr = [[0]*(n+1)] + [[0] +list(map(int, input().split())) for _ in range(n)]
# print(arr)

# 치킨집 개수 및 좌표 넣어두기
ch = []
home = []
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j] == 2:
            cnt +=1
            ch.append([i,j]) # 치킨집 좌표 저장
        if arr[i][j] == 1:
            home.append([i,j]) # 집 좌표 저장

total = 2*n*2*n # 가장 최소 값

dfs(0,[])
print(total)



