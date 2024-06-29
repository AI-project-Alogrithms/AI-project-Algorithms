# 연산자 끼워넣기: 43% 자꾸 틀리는데 정말 화남....모르겠음ㅠㅠㅠㅠ
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 최대 최소 정의
max_v = -10000001
min_v = 100000001

def dfs(n, ans, lst):
    global max_v, min_v
    if n==N:
        max_v = max(max_v, ans)
        min_v = min(min_v, ans)
        return

    if lst[0]<add : # add
        lst[0] += 1
        dfs(n+1, ans+arr[n], lst)
        lst[0] -= 1
    if lst[1]<sub: # sub
        lst[1]+=1
        dfs(n+1, ans-arr[n], lst)
        lst[1]-=1
    if lst[2]<mul : # mul
        lst[2]+=1
        dfs(n+1, ans*arr[n], lst)
        lst[2] -= 1
    if lst[3]<div: # div
        lst[3] += 1
        dfs(n+1, int(ans/arr[n]), lst)
        lst[3] -= 1
        #
        # if ans < 0: # 음수일때
        #     lst[3] += 1
        #     dfs(n+1, -(-ans//arr[n]), lst)
        #     lst[3] -= 1
        # else:
        #     lst[3] += 1
        #     dfs(n + 1, ans // arr[n], lst)
        #     lst[3] -= 1

# 수 개수, 수 리스트, [연사자 리스트]
N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

ans = arr[0]
dfs(1,ans,[0,0,0,0]) # 첫번재 수, count, 연산자 리스트
print(max_v)
print(min_v)