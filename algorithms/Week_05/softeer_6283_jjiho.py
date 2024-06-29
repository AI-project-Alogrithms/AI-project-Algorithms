# 8단 변속기 level 2
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def ch(n):
    if n == a:
        return "ascending"
    elif n == d:
        return "descending"
    else:
        return "mixed"
n = list(map(int, input().split()))
a = [1,2,3,4,5,6,7,8]
d = [8,7,6,5,4,3,2,1]
print(ch(n))
