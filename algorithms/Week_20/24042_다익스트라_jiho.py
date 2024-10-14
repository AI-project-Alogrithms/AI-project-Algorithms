# 횡단보도
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
INF = sys.maxsize

def dijkstra():
    q = [] # heapq 생성
    heapq.heappush(q, (0, 1)) # (시작 시간, 첫번째 위치)
    visited = [INF]*(N+1)
    visited[1] = 0 # 첫번째 위치 도달 최소 시간
    while q:
        time, node = heapq.heappop(q)
        # print("time, node", time, node)

        if time>visited[node]: continue # 최소 시간 보다 time이 크다면 패스
        for i, nnode in arr[node]:
            # print("i, nnode",i, nnode)
            tmp = (time-i)//M # 나눗셈 버림 방식임. 음수 나숫셈이라면 -1 더 되는 거임
            # print(time-i, (time-i)//M, tmp)
            if (time-i)%M!=0:
                tmp+=1
            ntime = i+tmp*M

            # ntime = i+((time-i)//M)*M if (time-i)%M == 0 else i+((time-i)//M+1)*M
            # print(ntime)
            if visited[nnode] > ntime+1:
                visited[nnode] = ntime+1 # 횡단 보도 건너는데 1분 걸림
                # print(ntime+1,nnode)
                # print(visited)
                heapq.heappush(q, (ntime+1, nnode))
    return visited[N]
N,M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    arr[a].append((i,b))
    arr[b].append((i,a))
# print(arr)

print(dijkstra())