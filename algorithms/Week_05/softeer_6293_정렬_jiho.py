# 징검다리: 최장 증가 부분 수열(LIS) 알고리즘
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def binary_search(target, lst):
    start, end = 0, len(lst)
    while start < end:
        mid = (start+end)//2 #중간 인덱스부터 시작
        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start #  만약 시작점과 끝점이 같다면 시작점을 반환


def lis(arr):
    lst = [arr[0]] # 수열의 첫번째 값을 저장
    for i in range(1, N): # 두번째부터 돌면서 LST의 가장 끝 값과 비교
        target = arr[i]
        if lst[-1] < target: # target값이 lst의 최댓값 보다 크다면
            lst.append(target)
        else: # 작다면 이분 탐색해서 제일 작은 위치 반환
            idx = binary_search(target, lst)
            lst[idx] = target
    return len(lst)

print(lis(arr))
