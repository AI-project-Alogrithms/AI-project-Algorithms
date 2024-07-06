# 숨바꼭질 3
"""
+1과 -1과 *2를 모두 똑같이 BFS로 탐색하게 된다면, +1로 찾은 칸은 *2로 갈 수 있었음에도 불구하고, 이미 방문 처리가 되어 있기에 *2로 찾을 수 없게 된다. 이를 해결하기 위해 *2를 더 먼저 처리
이를 해결하기 위해 queue에 push 할 때 queue.appendleft()를 사용하여 맨 왼쪽에 추가하는 방식으로 진행

"""
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
# -1 로 초기화 하는 걸로 바꿨더니 시간초과 안남..근데 정확한 이유는 모르겠음
def bfs(v):
  q = deque([v])
  while q:
    v =q.popleft()
    if v==k:
      return array[v]
    for next_v in (v-1,v+1,2*v):
      if 0<=next_v<MAX and array[next_v]==-1:
          if next_v == 2*v:
              array[next_v] = array[v]
              q.appendleft(next_v)
          else:
              array[next_v] = array[v]+1
              q.append(next_v)

MAX = 100001
n,k = map(int, input().split())
array = [-1]*MAX
array[n] = 0
print(bfs(n))