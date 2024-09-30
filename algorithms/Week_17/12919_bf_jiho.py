# A와 B 2
# 핵심: s-> t로 가는게 아닌 t->s로 가도록 해야 시간초과가 안남
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(t):
    global ans
    if len(t)==len(s):
        if t==s:
            ans = 1
        return
    if t[-1]=='A': # 마지막이 A면 그냥 제거
        dfs(t[:-1])
    if t[0]=='B': # T의 처음이 B라면 B제거 후, 뒤집기
        dfs(t[1:][::-1])

s = input().rstrip()
t = input().rstrip()
ans = 0
dfs(t)
print(ans)
