import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[] for _ in range(N)] for _ in range(N)]

# 방향: 오른쪽, 왼쪽, 위쪽, 아래쪽 (1, 2, 3, 4)
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

# hourse 배열을 (x, y, d) 형태로 저장
hourse = []
for i in range(K):
    r, c, d = map(int, input().split())
    dp[r-1][c-1].append(i) # 인덱스만 저장
    hourse.append([r-1, c-1, d-1])

def move_horse(horse_idx): # 말 인덱스
    x, y, d = hourse[horse_idx]

    # 새로운 위치 계산
    ni, nj = x + di[d], y + dj[d]

    # 체스판을 벗어나거나 파랑색일 경우
    if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 2:
        # 방향 반대로
        if d == 0 or d == 2:
            d += 1
        else:
            d -= 1
        hourse[horse_idx][2] = d
        ni, nj = x + di[d], y + dj[d]

        # 반대 방향도 막힌 경우 제자리
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 2:
            return False

    # 현재 위치에서 해당 말 위에 있는 말들을 모두 가져오기
    stack_idx = dp[x][y].index(horse_idx)
    moving_horses = dp[x][y][stack_idx:]
    dp[x][y] = dp[x][y][:stack_idx]

    # 빨강 경우: 순서 뒤집기
    if arr[ni][nj] == 1:
        moving_horses.reverse()

    # 새로운 위치에 말들 추가
    dp[ni][nj].extend(moving_horses)

    # 이동한 말들의 위치 갱신
    for idx in moving_horses: # 이동한 말들의 인덱스를 돌면서 말 업데이트
        hourse[idx][0] = ni
        hourse[idx][1] = nj

    # 말이 4개 이상 쌓이면 게임 종료 조건
    if len(dp[ni][nj]) >= 4:
        return True

    return False

cnt = 0
while cnt <= 1000:
    cnt += 1
    for i in range(K):
        if move_horse(i):
            print(cnt)
            sys.exit()
print(-1)
