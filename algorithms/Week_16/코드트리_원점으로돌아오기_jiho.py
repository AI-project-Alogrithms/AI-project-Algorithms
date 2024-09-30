# 백트래킹
# 그때그때 검사하는 방법도 있음 -> 이게 훨씬 빠름
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
# 재귀 깊이 제한 설정
sys.setrecursionlimit(10000)

def istrue(tmp):
    q = deque(tmp)
    # print(q)
    ci, cj = 0,0 # 원점
    d = -1 # 방향 전환
    while(q):
        ni, nj = q.popleft()
        # print(d)
        # 위, 아래 움직이는게 아니면 false
        if ci!=ni and cj!=nj:
            return False
        else:
            # 위 아래라면
            if ci==ni:
                if cj<nj: dr = 0 # 위
                else: dr = 1 # 아래
            elif cj==nj:
                if ci<ni: dr = 2 # 오른쪽
                else: dr = 3 # 왼쪽
            ci, cj = ni, nj
            if d!=dr: # 방향 전환이 있다면
                d = dr
            else:
                return False
    return True


def dfs(n, tmp, v):
    global cnt
    if n==N: # 모든 좌표가 다 들어갔으면
        ti, tj = tmp[-1] # 마지막 좌표 먼저 검사
        if (ti==0 or tj==0) and istrue(tmp+[(0,0)]):
            # print(tmp)
            cnt+=1
        return
    for i in range(N):
        if len(tmp)==0 and lst[i][0]!=0 and lst[i][1]!=0: continue
        if v[i]==0:
            v[i]=1
            dfs(n+1, tmp+[lst[i]],v)
            v[i]=0


N = int(input())
lst = []
cnt = 0
for _ in range(N):
    i,j = map(int, input().split())
    lst.append((i,j))
v = [0]*N
dfs(0, [], v)
print(cnt)