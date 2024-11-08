# 반도체 설계
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bisect_left(arr, val):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > val: # 배열 값이 value보다 크면 더 작은 인덱스 찾기
            end = mid-1
        else:
            start = mid+1
    return start

n = int(input())
lst = list(map(int, input().split()))

link = []
for d in lst:
    if not link or link[-1]<d:
        link.append(d)
    else:
        link[bisect_left(link, d)] = d
    print(len(link))

