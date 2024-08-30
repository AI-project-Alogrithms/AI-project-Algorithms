# 연탄의 크기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

r = 2 # 반지름 최소값
ans= 0 # 최대개수
while(r<=max(lst)):
    cnt = 0
    for i in lst:
        if i%r==0: # 배수이면
            cnt +=1
    ans = max(ans, cnt)
    r +=1
print(ans)