# 연산자 끼워넣기
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(exp, idx, lst):
    global max_v, min_v
    if idx == N:
        max_v = max(max_v, eval(exp))
        min_v = min(min_v, eval(exp))
        return
    if lst[0] < add:
        lst[0] +=1 # 덧셈 사용
        dfs(exp+"+"+str(a[idx]), idx+1, lst)
        lst[0] -=1 # 덧셈 사용 풀기
    if lst[1] < minus:
        lst[1] +=1 # - 사용
        dfs(exp+"-"+str(a[idx]), idx+1, lst)
        lst[1] -=1 # - 사용 풀기
    if lst[2] < mul:
        lst[2] +=1 # * 사용
        dfs(exp+"*"+str(a[idx]), idx+1, lst)
        lst[2] -=1 # * 사용 풀기
    if lst[3] < div:
        lst[3] +=1 # * 사용
        dfs(exp+"//"+str(a[idx]), idx+1, lst)
        lst[3] -=1 # * 사용 풀기

N = int(input())
a = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())
max_v = -1000000000
min_v = 1000000000
dfs(str(a[0]), 1, [0,0,0,0]) # 첫번째 수, idx, 연산자 리스트
print(max_v)
print(min_v)