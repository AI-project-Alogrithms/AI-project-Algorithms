# 게임 # x가 너무 커도 이분탐색은 log(n)이라는 믿음을 갖고 하자!
"""
10억 이상 -> 이분 탐색
"""
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(start, end):
    while(start<=end):
        mid = (start+end)//2 # 추가 게임 수 = 추가 승리 수 (최소가 될때까지 반복)
        if ((y+mid)*100//(x+mid)) > Z: # Z를 넘었을 경우
            ans = mid
            end = mid-1
        else: # 아닐경우
            start = mid + 1
    return ans

x, y = map(int, input().split())
Z = (y*100)//x # 승률

if Z>=99: #99퍼 일땐 더이상 승률이 안오름
    print(-1)
else:
    ans = 0  # count
    start = 1 # 최소 추가 승
    end = 1000000000 # 최대 추가 승
    print(binary_search(start, end)) # 승률 계산하기