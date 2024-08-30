# 나무공격
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(2):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        for j in range(m):
            if arr[i][j] ==1 :
                arr[i][j] = 0
                break
ans = 0
for i in arr:
    ans += i.count(1)
print(ans)