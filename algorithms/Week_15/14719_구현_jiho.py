# 빗물
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 해당 칸 기준 좌측에서 가장 높은 값과 우측에서 가장 높은 값 중 더 작은 값에서 해당 칸 값 빼기
H, W = map(int, input().split())
lst = list(map(int, input().split()))
cnt=0
for i in range(1,W-1):
    tmp = min(max(lst[:i]), max(lst[i+1:]))
    if tmp > lst[i]: # 가장 큰 블록일 경우 음수가 나옴 따라서 양수일때만 cnt
        cnt+=tmp-lst[i]
    # cnt += min(max(lst[:i]), max(lst[i+1:]))-lst[i]
print(cnt)