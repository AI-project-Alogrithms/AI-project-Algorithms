# 계란으로 계란치기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
"""
백트래킹은 가지치기를 항상 생각하기!!
- 남은 횟수에서 모두 깨도 (N-n)*2 => 해도 정답보다 같거나 작으면 더이상 갈 이유가 없음
"""
def dfs(n, cnt):
    global ans
    # 가지치기
    if ans >= (cnt+(N-n)*2): # 끝까지 진행해도 정답 갱신 불가인 경우 끝내기
        return
    if n==N:# 모든 계란을 부딪힌 경우
        ans = max(ans, cnt)
        return
    if arr[n][0] <= 0: # 내가 손에 든 계란이 깨진 경우, 다음 계란으로 가기
        dfs(n+1, cnt)
    else: # 현재 계란이 안깨진 상태인 경우
        flag = False # 하나도 안부딪힌 경우 => 다음단계가기
        for j in range(N):
            if n==j or arr[j][0] <=0: continue
            flag = True # 부딪힌 경우
            # 계란 깨기
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n+1, cnt+int(arr[n][0]<=0) + int(arr[j][0]<=0))
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]
        if flag == False: # 한번도 안부딪혀도 다음 단계 가기
            dfs(n+1, cnt)




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0,0) # 계란 인덱스, 깨진 계란 개수
print(ans)

