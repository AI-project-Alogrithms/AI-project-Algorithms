# 빵집
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

di = [-1,0,1]
dj = [1,1,1]

def dfs(ci,cj):
    if cj == C-1:
        return True

    for d in range(3):
        ni, nj = ci+di[d], cj+dj[d]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj]!='x' and visited[ni][nj]==0:
            visited[ni][nj] = 1 # 방문 표시
            if dfs(ni, nj):
                return True
            # visited[ni][nj] = 0 # 방문 표시 해제 ==> 이걸 할 필요가 없음 애초에 맨 윗칸부터 하면 두번 방문할 필요가 없기 때문임
    return False

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

visited = [[0]*C for _ in range(R)]
cnt = 0
for i in range(R):
    if dfs(i, 0):
        cnt +=1
print(cnt)