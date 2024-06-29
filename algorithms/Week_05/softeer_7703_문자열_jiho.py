# x marks the Spot
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N= int(input())
ans = []
for i in range(N):
    S, T = map(str, input().rstrip().split())
    save = 0
    T = list(T)
    for idx, value in enumerate(S):
        if value =='x' or value == 'X':
            save = idx
            ans.append(T[save].upper())
            break
print("".join(map(str, ans)))