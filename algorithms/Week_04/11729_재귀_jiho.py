# 하노이 탑
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def hanoi(n, start, end, two):
    # n=1이라면
    if n==1:
        lst.append((start, end))
        return
    # 가장 큰 원반을 제외한 나머지 원반을 보조기둥으로 옮기기 n-1개
    hanoi(n-1, start, two, end)
    lst.append((start, end))
    # print(start, '-> ', end)
    # 보조 기둥을 시작기둥, 시작기둥을 보조기둥으로 바꾸고 진행하기
    hanoi(n-1, two, end, start)

n = int(input())
lst = []
hanoi(n, 1, 3, 2) # n개의 기둥을 1 -> 3으로 옮기는데 2를 보조로 사용하겠다.
print(len(lst))
for i in lst:
    print(" ".join(map(str, i)))
