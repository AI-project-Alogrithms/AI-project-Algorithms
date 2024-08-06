# 두 배열의 합 -> 이분탐색
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import Counter

def binary_search_left(arr, t):
    low, high = 0, len(arr)
    while(low<high):
        mid = (low+high)//2
        if arr[mid]< t:
            low = mid+1
        else:
            high = mid
    return low

def binary_search_right(arr,t):
    low, high = 0, len(arr)
    while (low< high):
        mid = (low+high)//2
        if arr[mid]<=t:
            low = mid+1
        else:
            high = mid
    return low

T = int(input()) # 최종 만족되어야하는 값
n = int(input()) # 배열 A 원소 개수
alst = list(map(int, input().split()))
m = int(input()) # 배열 B 원소 개수
blst = list(map(int, input().split()))
asum, bsum = [], []
ans = 0 # 출력값
# 배열 A의 모든 부배열의 합
for i in range(n):
    s = 0
    for j in range(i, n):
        s += alst[j]
        asum.append(s)

# 배열 B의 모든 부배열의 합
for i in range(m):
    s = 0
    for j in range(i, m):
        s += blst[j]
        bsum.append(s)

asum.sort();bsum.sort() # 이분탐색을 위한 정렬

for i in range(len(asum)): # asum 인덱스들을 돌동안
    left = binary_search_left(bsum, T-asum[i])
    right = binary_search_right(bsum, T-asum[i])
    ans += right-left

print(ans)
"""
Counter 이용한 풀이
c = Counter() # Counter 정의
for s in range(n):
    for e in range(s,n):
        c[sum(alst[s:e+1])] +=1 # 배열 A의 모든 부배열의 합을 COUNT로 세기

for s in range(m):
    for e in range(s,m):
        t = T-sum(blst[s:e+1]) # 타겟값 T에서 B 부배열의 합 뺀 값
        # t가 A의 부배열 C에 존재하면 ans +=1
        ans += c[t]
print(ans)
"""


