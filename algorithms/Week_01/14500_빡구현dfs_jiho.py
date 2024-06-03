import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
# arr = [[1, 2, 3, 4, 5],
#        [5, 4, 3, 2, 1],
#        [2, 3, 4, 5, 6],
#        [6, 5, 4, 3, 2],
#        [1, 2, 1, 2, 1]]

# 테르로미노 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * m for _ in range(n)]


def dfs(x, y, c_sum, cnt):
    global max_sum

    if cnt == 4:
        max_sum = max(max_sum, c_sum)
        return
    # 4방향으로 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]  # 다음 방문
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True  # 방문 처리
            # c_sum += arr[x][y]
            # cnt += 1
            dfs(nx, ny, c_sum + arr[nx][ny], cnt + 1)
            visited[nx][ny] = False  # 방문 처리 제거


def check_shape(x, y):
    global max_sum
    tmp = arr[x][y]
    add_list = []
    for i in range(4):  # 모든 방향 탐색
        nx, ny = x + dx[i], y + dy[i]  # 다음 방문
        if 0 <= nx < n and 0 <= ny < m:
            add_list.append(arr[nx][ny])
    # print(add_list)
    if len(add_list) == 4:  # 네 방향 모두 들어왔다면 가장 작은 수 제거 후 모두 더하기
        add_list.sort()
        max_sum = max(max_sum, sum(add_list[1:]) + tmp)
        # print(add_list.pop(0))
    elif len(add_list) == 3:  # 하나만 있다면 다 더하기
        max_sum = max(max_sum, sum(add_list) + tmp)
    # return # 길이가 2 이하면 return


max_sum = 0  # 최대 합 저장
for i in range(n):
    for j in range(m):
        visited[i][j] = True  # 현재 배열 원소 방문
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = False
        check_shape(i, j)
print(max_sum)
