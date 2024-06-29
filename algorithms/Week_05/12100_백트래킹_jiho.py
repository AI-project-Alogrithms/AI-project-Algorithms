# 2048
import sys
# sys.setrecursionlimit(5000)
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def move(arr):
    # 행단위로 이동 (같은 값 합치기)
    for i in range(len(arr)):
        # 행 개수만큼 처리
        num = 0 # 넣어야될 기준 숫자 num과 같으면 두배 tlst에 넣기
        tlst = []
        for n in arr[i]: # 해당 행에서 숫자 꺼내기
            if n==0: continue # 빈칸 처리 안함
            if n==num: # 기준 숫자와 동일하면
                tlst.append(num*2)
                num = 0
            else: # 기준 숫자와 다르면
                if num==0: # 기준이 처음이라면
                    num = n # n으로 바꾸기
                else: # 기준이 처음이 아니라면
                    tlst.append(num)
                    num = n
        # 종료 후 기준 숫자 있으면 tlist에 추가, 남은 자리 0으로 채움
        if num > 0: # 마지막 숫자 추가
            tlst.append(num)
        arr[i] = tlst+[0]*(N-len(tlst)) # tlst남은 길이 0으로 채우기


def dfs(n, arr):
    global ans
    if n==5: # 종료 조건
        ans = max(ans, max(map(max, arr))) # arr 중 가장 큰 값으로 갱신
        return
    # 상하좌우 각각 해주기
    # 좌측이동
    narr = [lst[:] for lst in arr] # 딥카피해서 전달
    move(narr)
    dfs(n+1, narr)

    narr = [lst[::-1] for lst in arr]  # 우측 방향
    move(narr)
    dfs(n + 1, narr)

    arr_t = list(map(list, zip(*arr))) # 전치행렬 만들기 # 열 -> 행으로
    narr = [lst[:] for lst in arr_t] # 상방향
    move(narr)
    dfs(n+1, narr)

    narr = [lst[::-1] for lst in arr_t] # 하 방향
    move(narr)
    dfs(n+1, narr)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
# print(max(map(max, arr)))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 상하좌우 네방향 가능한 모든 경우 처리
ans = 0
dfs(0, arr) # 단계, arr
print(ans)
