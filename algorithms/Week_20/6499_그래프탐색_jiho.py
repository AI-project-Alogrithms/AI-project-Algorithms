# 텀프로젝트 => 사이클
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def dfs(ci):
    global cnt
    visited[ci] = True
    cycle.append(ci)
    if visited[lst[ci]]: # True라면
        if lst[ci] in cycle: # cycle에 들어있다면
            # print(cycle)
            cnt+=cycle[cycle.index(lst[ci]):]
        return
    else:
        dfs(lst[ci])



T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0]+list(map(int, input().split()))
    visited = [True]+[False]*(N)
    cnt = [] # 팀을 만들 학생 후
    for i in range(1, N+1):
        # target = i

        if not visited[i]:
            cycle = [] # 팀
            dfs(i)
            # print(visited)

    print(N-len(cnt))

