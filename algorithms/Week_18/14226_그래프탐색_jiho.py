# 이모티콘 => bfs
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(x_screen, x_clip):
    q = deque()
    q.append((x_screen, x_clip))
    visited[x_screen][x_clip] = 0
    while q:
        x_screen, x_clip = q.popleft()
        if x_screen==S:
            print(visited[x_screen][x_clip])
            break
        arr = [(x_screen, x_screen),
               (x_screen+x_clip, x_clip),
               (x_screen-1, x_clip)] # 복사, 붙여넣기, 삭제
        for screen, clip in arr:
            if 0<=screen<1001 and 0<=clip<1001 and visited[screen][clip]==-1:
                q.append((screen, clip))
                visited[screen][clip] = visited[x_screen][x_clip]+1

S = int(input()) # s개 만들기
visited = [[-1]*1001 for _ in range(1001)]
bfs(1,0) # x_screen, x_clip
