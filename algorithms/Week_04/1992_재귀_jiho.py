# 쿼드트리
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def code_tree(r,c,n):
    current = arr[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if current != arr[i][j]:
                half = n//2
                ct.append('(')
                code_tree(r,c,half)
                code_tree(r,c+half, half)
                code_tree(r+half, c, half)
                code_tree(r+half, c+half, half)
                ct.append(')')
                return
    ct.append(current)
    return

n = int(input())
arr=[list(map(int, input().rstrip())) for _ in range(n)]
ct=[]
code_tree(0,0,n)
print("".join(map(str, ct)))