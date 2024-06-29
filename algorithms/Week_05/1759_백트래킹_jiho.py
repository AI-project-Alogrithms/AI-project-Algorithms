# 암호 만들기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, lst):
    if n==C:
        if len(lst) == L:
            mo = 0
            ja = 0
            for i in range(L):
                if lst[i] in mo_lst:
                    mo +=1
                else:
                    ja +=1
            if mo >=1 and ja >= 2:
                print("".join(map(str, lst)))
        return
    dfs(n+1, lst+[arr[n]]) # 넣고
    dfs(n+1, lst) # 안넣고

L, C = map(int, input().split())
arr = list(map(str, input().rstrip().split()))
arr.sort()
mo_lst = ['a','e','i','o','u']

dfs(0, [])