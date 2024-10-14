# 물통
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(a,b,c):
    global ans
    # 방문한 set 모두 저장
    if (a,b,c) in visited:
        return
    visited.add((a,b,c))

    # a==0일때의 c의 값 저장
    if a==0:
        ans.add(c)

    # a->b
    if b+a>B:
        dfs(a-(B-b), B, c)
    else:
        dfs(0, a+b, c)

    # a -> c
    if c+a>C:
        dfs(a-(C-c), b, C)
    else:
        dfs(0, b, a+c)

    # b->a
    if b+a>A:
        dfs(A, b-(A-a), c)
    else:
        dfs(a+b, 0, c)

    # b->c
    if b+c>C:
        dfs(a, b-(C-c), C)
    else:
        dfs(a, 0, b+c)

    # c -> a
    if c+a>A:
        dfs(A, b, c-(A-a))
    else:
        dfs(a+c, b, 0)

    # c->b
    if b+c>B:
        dfs(a, B, c-(B-b))
    else:
        dfs(a, b+c, 0)


A,B,C = map(int, input().split())
visited = set()
ans = set()


dfs(0,0,C)
ans = sorted(ans)
print(" ".join(map(str, ans)))





