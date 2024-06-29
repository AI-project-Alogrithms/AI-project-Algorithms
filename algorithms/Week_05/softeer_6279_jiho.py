# 스마트 물류: 완전 탐색, 가장 가까운 것부터 처리!
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n,k = map(int, input().split())
line = list(str(input()))
print(line)
visited = [False]*n
for i in range(n):
    if line[i]=='P': # 로봇이면
        for j in range(i-k, i+k+1):
            if (i==j) or (j<0) or (j>=n): continue # 범위 밖이고, 자기자신일땐 pass
            if line[j] == 'H' and not visited[j]:
                # 제품이고 아직 방문 전이면
                visited[j] = True
                print(visited)
                break
count = 0
for i in visited:
    if i == True:
        count +=1
print(count)


