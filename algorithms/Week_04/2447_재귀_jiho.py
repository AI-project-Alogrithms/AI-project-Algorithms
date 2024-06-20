# 별 찍기 - 10
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def star(n):
    if n==1:
        return '*'
    half = n//3 # 3
    x = star(half)
    result = []
    for i in x:
        result.append(i*3)
    for i in x:
        result.append(i + ' '*(n//3) + i)
    for i in x:
        result.append(i*3)
    return result
n = int(input())
arr = star(n)
# print(arr)
for i in arr:
    print(i)


