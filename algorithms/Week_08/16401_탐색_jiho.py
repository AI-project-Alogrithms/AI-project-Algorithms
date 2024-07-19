# 과자 나눠주기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def search(start, end):
    while(start <= end):
        # print("start: ", start)
        mid = (start + end) //2
        # print("mid: ", mid)
        cnt = 0
        for s in lst:
            if mid<=s:
                cnt += (s//mid)
        # print("cnt: ", cnt)

        if cnt >= M:
            start  = mid +1
        else:
            end = mid-1
    return end

M, N = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
start, end = 1, lst[-1] # 길이가 맞음
print(search(start, end))
