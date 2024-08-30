# 사물인식최소면적산출프로그램
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 색깔에 따른 좌표 저장
N, K = map(int, input().split())
points = [[] for _ in range(K)]

for _ in range(N):
    x, y, k = map(int, input().split())
    points[k - 1].append((x, y))  # k-1로 인덱스 맞춤

# 초기값 설정
min_area = sys.maxsize  # 최소 면적을 무한대로 초기화


# DFS 탐색 함수
def dfs(depth, min_x, max_x, min_y, max_y):
    global min_area

    # 기저 사례: 모든 색깔을 다 선택한 경우
    if depth == K:
        current_area = (max_x - min_x) * (max_y - min_y)
        min_area = min(min_area, current_area)
        return

    # 현재 색깔(depth)에서 모든 좌표를 순회
    for x, y in points[depth]:
        # 새로운 직사각형의 경계 업데이트
        new_min_x = min(min_x, x)
        new_max_x = max(max_x, x)
        new_min_y = min(min_y, y)
        new_max_y = max(max_y, y)

        # 현재까지 구한 면적이 이미 최소 면적보다 크면 더 이상 탐색하지 않음
        if (new_max_x - new_min_x) * (new_max_y - new_min_y) >= min_area:
            continue

        # 다음 색깔(depth+1)로 DFS 진행
        dfs(depth + 1, new_min_x, new_max_x, new_min_y, new_max_y)


# 초기 탐색 시작
for x, y in points[0]:
    dfs(1, x, x, y, y)

# 결과 출력
print(min_area)
