# 주사위 윷놀이
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, sum):
    global ans
    if n==10: # 10번 다 던졌다면
        ans = max(ans, sum)
        return

    # 하부 호출 (이동, 하부 호출)
    for j in range(4):
        start = v[j] # j번말의 현재 위치
        cur = adj[start][-1] # 한칸 이동(갈림길의 경우 시작 위치에 따라 다름)
        for _ in range(1, nlst[n]): # 나머지 칸 이동
            cur = adj[cur][0]

        # 목적지 이거나, 다른 말이 없는 경우 이동 가능
        if cur == 32 or cur not in v:
            v[j] = cur # 말 위치 바꾸기
            dfs(n+1, sum+score[cur])
            v[j] = start # 말 위치 원래대로 바꾸기




# 인접 리스트 만들기 (이때, 갈림길에서 뒤에꺼로 가도록 하기)
#       0   1   2   3   4    5     6   7   8   9      10    11   12   13   14    15    16    17   18   19   20   21   22  23    24   25  26    27   28  29  30  31
adj = [[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,27],[12],[13],[14],[15],[16,29],[17],[18],[19],[20],[32],[22],[23],[24],[25],[26],[20],[28],[24],[30],[31],[24],[32],[32],[32],[32],[32]]
score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,30,35,22,24,28,27,26,0]
nlst = list(map(int, input().split())) # 주사위에서 나올 수
v = [0,0,0,0] # 말의 현재 위치 저장
ans = 0
dfs(0,0)
print(ans)