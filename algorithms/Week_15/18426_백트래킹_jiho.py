# 감시 피하기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
from itertools import combinations

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(tq, lst):
    arr_copy = [a[:] for a in arr]
    for i, j in lst:
        arr_copy[i][j] = 'O'
    for ti, tj in tq:
        # ti, tj = tq.popleft()
        # 상
        for x in range(ti, -1,-1):
            if arr_copy[x][tj] == 'O':
                break
            elif arr_copy[x][tj] == 'S':
                return False
        # 하
        for x in range(ti, N, 1):
            if arr_copy[x][tj] == 'O':
                break
            elif arr_copy[x][tj] == 'S':
                return False

        # 좌
        for y in range(tj, -1, -1):
            if arr_copy[ti][y] == 'O':
                break
            elif arr_copy[ti][y] == 'S':
                return False

        # 우
        for y in range(tj, N, 1):
            if arr_copy[ti][y] == 'O':
                break
            elif arr_copy[ti][y] == 'S':
                return False
    # print("true list", lst)
    return True


def dfs(n, lst, start):
    global ans
    if n==3:
        # print(lst)
        # 선생님의 감시를 벗어나는지 확인
        if bfs(teacher, lst):
            ans = 'YES'
        return
    for i in range(start, len(empty)):
        if (empty[i][0],empty[i][1]) not in lst:
            dfs(n+1, lst+[(empty[i][0],empty[i][1])], i+1) # 조합

N = int(input())
arr = [list(input().rstrip().split()) for _ in range(N)]

empty = []
teacher = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            empty.append((i,j))
        elif arr[i][j] == 'T':
            teacher.append((i,j))
# print(empty)
# print(teacher)
ans = 'NO'
dfs(0,[],0)
print(ans)