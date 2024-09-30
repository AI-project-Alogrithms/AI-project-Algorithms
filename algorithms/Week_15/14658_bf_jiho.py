# 하늘에서 별똥별이 빗발친다
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 트램블린을 기준으로하면 시간 초과, 별 두개를 기준으로 해당 별들의 가장 왼쪽 상단 좌표로 만들기

def func(i,j):
    cnt = 0
    for x, y in star:
        if i <= x <= i + l and j <= y <= j + l:
            cnt += 1
    return cnt

n,m,l,k = map(int, input().split())
star = []
ans = 0
for _ in range(k):
    a,b = map(int, input().split())
    star.append((a, b))
for i in range(k):
    for j in range(k):
        # 가장 왼쪽 상단 좌표
        x = min(star[i][0], star[j][0])
        y = min(star[i][1], star[j][1])
        ans = max(ans, func(x,y))
print(k-ans) # 부딪히는 별 개수
