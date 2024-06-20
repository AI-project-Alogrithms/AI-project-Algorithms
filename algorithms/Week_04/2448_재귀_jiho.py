# 별 찍기 - 11
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def draw(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    half = n // 2
    star = draw(half)
    result = []

    # 상단 부분
    for s in star:
        result.append(" " * half + s + " " * half)

    # 하단 부분
    for s in star:
        result.append(s + " " + s)

    return result


n = int(input().strip())
result = draw(n)
for line in result:
    print(line)
