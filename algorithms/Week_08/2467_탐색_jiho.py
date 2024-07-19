# 용액
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution():
    start = 0
    end = n-1
    ans = abs(lst[0]+lst[-1]) # 차이 값 초기화
    final = [lst[0], lst[-1]] # 정답 초기화
    while(start<end):
        result = lst[start] + lst[end]
        if abs(result) <= ans:
            ans = abs(result) # 현재 ans보다 해당 값이 더 작거나 같다면
            final = [lst[start], lst[end]]
            if ans == 0: break # 0과 가장 가까우니까 그만하기
        if result<0: # 0보다 작다면 좀더 크게 만들기
            start +=1
        else:
            end -=1
    print(*final)

n = int(input())
lst = list(map(int, input().split()))

solution()
