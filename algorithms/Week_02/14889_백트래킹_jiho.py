# 스타트와 링크
import sys
from sys import stdin

# sys.stdin = open("Week_02/input.txt", "r")
input = sys.stdin.readline

from collections import deque, defaultdict

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 한 팀당 인원
m = n // 2

answer = 100 * m * m  # 최대 차이
# people 총 n 명


def dfs(people, alist, blist):
    global answer
    if people == n:
        if len(alist) == len(blist):  # 동일한 수로 나눠졌을 때
            asum = bsum = 0  # 총 능력치 합
            for i in range(m):
                for j in range(m):
                    asum += arr[alist[i]][alist[j]]
                    bsum += arr[blist[i]][blist[j]]
            answer = min(answer, abs(asum - bsum))
        return
    dfs(people + 1, alist + [people], blist)  # a팀
    dfs(people + 1, alist, blist + [people])  # b팀


dfs(0, [], [])
print(answer)
