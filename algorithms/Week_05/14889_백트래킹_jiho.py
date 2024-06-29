# 스타트와 링크
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, start, link):
    global min_v
    if n==N:# 모든 선수들 다 씀
        if len(start) == N//2: # 같은 수가 들어갔을 때
            s_sum = 0
            l_sum = 0
            for i in range(N//2):
                for j in range(N//2):
                    s_sum += arr[start[i]][start[j]]
                    l_sum += arr[link[i]][link[j]]
            min_v = min(min_v, abs(s_sum-l_sum))
            # print(min_v)
        return
    dfs(n+1, start+[n], link)
    dfs(n+1, start, link+[n])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 4000000
dfs(0, [], []) # n, start, link
print(min_v)