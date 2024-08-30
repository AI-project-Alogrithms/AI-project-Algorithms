# 고층 건물 => 기울기 이용 (오른쪽: 기울기가 앞에 꺼보다 커야 볼 수 있음, 왼쪽: 기울기가 앞에꺼보다 작어져야 볼 수 있음)
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1) # 기울기

n = int(input())
lst = list(map(int, input().split()))

ans = 0
for i, y1 in enumerate(lst):
    x1 = i+1 # index가 1부터 시작
    # 자기 위치에서 오른쪽으로 볼 수 있는 빌딩 수
    right = None
    v_right = 0 # 볼 수 있는 수 초기화
    for j in range(i+1, n+1):
        if j==n: break
        x2 = j+1 # 인덱스 맞추기
        y2 = lst[j] # 높이
        slope_right = slope(x1, y1, x2, y2) # 기울기 구하기
        if right is None or right<slope_right:
            # 구해진 기울기가 그 앞 기울기 보다 크다면 cnt+1
            right = slope_right
            v_right+=1
    # 왼쪽에서 볼 수 있는 빌딩 수
    left = None
    v_left = 0
    for j in range(i-1, -1, -1): # 왼쪽으로 한칸씩 이동
        if j==-1: break
        x2 = j+1
        y2 = lst[j]
        slope_left = slope(x1, y1, x2, y2)
        if left is None or left > slope_left:
            left = slope_left
            v_left +=1
    if (v_left+v_right)>ans:
        ans  = v_left+v_right
print(ans)
