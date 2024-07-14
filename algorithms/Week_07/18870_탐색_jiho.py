# 좌표 압축
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def search(item): # arr에서 자기보다 작은 거 몇개인지 세기 -> 해당 인덱스 자리가 그 개수와 동일함
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = (start + end)//2
        if arr[mid] == item:
            return mid
        elif arr[mid]<item:
            start = mid+1
        else:
            end = mid-1
    return start

n = int(input())
lst = list(map(int, input().split()))

arr = sorted(set(lst)) # 겹치는게 있으면 안세니까 set으로 중복 제거하기
ans = []
for item in lst:
    num = search(item)
    ans.append(num)
print(" ".join(map(str, ans)))