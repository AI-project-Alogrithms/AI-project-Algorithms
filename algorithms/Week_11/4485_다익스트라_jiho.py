# 녹색 옷 입은 애가 젤다지?
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq

def dijkstra(i,j):
    q = []
    heapq.heappush(q, (arr[i][j], i,j))
    cost_lst[i][j] = arr[i][j]
    while(q):
        weight, ci, cj = heapq.heappop(q)
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni<N and 0<= nj<N:
                if weight > cost_lst[ni][nj] : continue
                cost = arr[ni][nj] + weight
                if cost < cost_lst[ni][nj]:
                    cost_lst[ni][nj] = cost
                    heapq.heappush(q, (cost, ni, nj))
    return cost_lst[-1][-1]
cnt = 0
while(True):
    cnt +=1
    N = int(input())
    if N==0: break
    arr =[list(map(int, input().split())) for _ in range(N)]
    cost_lst = [[1e9]*N for _ in range(N)]
    print(f"Problem {cnt}: {dijkstra(0,0)}")