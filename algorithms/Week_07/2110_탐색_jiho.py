# 공유기 설치 -> 이분 탐색
"""
10억 이상 -> 이분 탐색
"""
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(arr, start, end):
    while(start<=end):
        mid = (start+end)//2 # 최소거리 지정
        cnt = 1 # 공유기 개수 초기화, 항상 처음 지점에 놔야 최대거리 구해짐
        current = arr[0]
        for i in range(1, len(arr)):
            if arr[i]- current >= mid:
                cnt +=1
                current = arr[i]
        if cnt >= C: # 공유기 개수가 지정된 수보다 많거나 같다면
            global ans
            start = mid+1
            ans = mid
        else:
            end = mid-1 # 최소거리를 더 작게 해야됨 (공유기가 다 설치가 안됐다면)
    return ans

N, C = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()
start = 1 # 최소거리일때
end = arr[-1]-arr[0] # 최대거리
ans = 0
print(binary_search(arr, start, end))

