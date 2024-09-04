import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def score(a):
    if len(a)==1:
        return 0
    else:
        cnt = 0
        for i in range(len(a)):
            for j in range(len(a)):
                cnt+=arr[a[i]][a[j]]
        return cnt

def dfs(n, start, link):
    global ans
    if n==N:
        if len(start)>0 and len(link)>0:
            # print("score(start): ", score(start))
            # print("score(link): ", score(link))
            # print("ans: ", ans)
            ans = min(ans, abs(score(start) - score(link)))
        return
    dfs(n+1, start+[n], link)
    dfs(n+1, start, link+[n])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 10**9
dfs(0, [], [])
print(ans)
