# Gaaaaaaaaaarden
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
"""
tlst와 lst를 같은 것으로 생각하고 bfs에 넘겨주는게 확실한듯함. 
백트레킹: 가능한 경우 => 빨강, 초록, 안뿌리기
==> 마지막 정답 처리 하는 거 n==TC: rcnt==RC, gcnt==GC => 정답 처리
bfs할때, 하나는 음수로, 하나는 양수로 뻗어나가고 abs가 같은 경우 꽃이 피는 걸로 하면 됨
- 이동할 장소 처음 방문v[]==0 => r: -1 / g: 1 ==> 만약 동시를 만족하고 싶다면 음수, 양수 사용하기!
- 뭔가 적혀있다. v[]!=0=> if abs()==; 꽃피면 => 25000 
"""

def flower(tlst): # q:채울때, -1, 1 넣어주기 lst에 죄표 저장
    q = deque()
    v = [[0]*(M+2) for _ in range(N+2)] # 단순 방문 여부
    # 큐에 초기데이터 삽입 및 v 표시
    for i in range(TC):
        if tlst[i]==0: continue # 넣어줄 필요 없음
        ti, tj = position[i] # 좌표 꺼내기
        q.append((ti, tj))
        v[ti][tj]= tlst[i] # -1,1 넣어주기 => rg구분
    cnt = 0 # 꽃 개수
    while(q):
        ci, cj = q.popleft()
        if v[ci][cj] == 25000: continue # 이미 꽃을 피웠다면 건너뛰기

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if arr[ni][nj]==0 or v[ni][nj]==25000: # 호수 아님, 꽃이 아니면 예외 처리
                continue
            if v[ni][nj]==0:# 미방문
                if v[ci][cj] < 0: # r: 1감소
                    v[ni][nj] = v[ci][cj]-1
                    q.append((ni,nj))
                elif v[ci][cj] > 0: # g: 1증가
                    v[ni][nj] = v[ci][cj]+1
                    q.append((ni,nj))
            else: # 방문한 경우 => 꽃 체크
                if v[ci][cj] < 0: # r 이면 => 그자리에 g이 있는지 체크
                    if v[ni][nj]+v[ci][cj]-1 == 0: # 꽃이 피면
                        cnt +=1
                        v[ni][nj] = 25000
                else: # g면
                    if v[ni][nj]+v[ci][cj]+1 == 0: # 꽃이 피면
                        cnt +=1
                        v[ni][nj] = 25000
    return cnt


def dfs(n, rcnt, gcnt, tlst):#  빨간색, 안뿌리거나, 초록색
    global ans
    if n==TC:
        if gcnt ==G and rcnt==R:
            # 배양액 퍼트리기
            cnt = flower(tlst) # 현재 위치에서 배양액을 뿌렸을 때 나오는 꽃 개수 return
            ans = max(ans, cnt)
        return
    # Red를 부르는 경우, green을 부르는 경우, 안뿌리는 경우
    dfs(n+1, rcnt+1, gcnt, tlst+[-1]) # tlst: 고르면 -1, green 고르면 1, 안고르면 0 넘겨주기
    dfs(n+1, rcnt, gcnt+1, tlst+[1])
    dfs(n+1, rcnt, gcnt, tlst+[0])


N, M, G, R = map(int, input().split())
arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
position = [] # 배양액을 놓을 수 있는 위치 미리 저장
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == 2: # 배양액을 놓을 수 있는 위치이면
            position.append((i,j))
TC = len(position) # 총 위치 개수

v = [[0]*M for _ in range(N)]
ans = 0
# 가능한 모든 장소에 배양액 뿌리는 방법 순회
dfs(0,0,0,[]) # n, rcnt, gcnt, tlst
print(ans)