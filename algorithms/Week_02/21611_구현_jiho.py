# 마법사 상어와 블리자드
import sys
from sys import stdin

# sys.stdin = open("Week_02/input.txt", "r")
input = sys.stdin.readline

from collections import deque, defaultdict


# # nxn, 블리자드 m번
n, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

# n = 7
m = n // 2  # 중앙 위치
# arr = [[0 for _ in range(n)] for _ in range(n)]


# 왼쪽 방향부터 반시계 달팽이
# dr = [0,1,2,3,4]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

flag = 0  # 뱡향 전환
cnt = 0  # cnt가 cnt_max가 될때마다 방향전황
cnt_max = 1  # 1부터 cnt_max가 되면 방향 바꾸기
ci, cj = m, m  # 중앙 좌료 초기화
dr = 0  # 뱡항 왼쪽 부터 시작
pos = []  # 2차원을 1차원으로 만들기, 1차원 리스트에서 pos 참조해서 달팽이 읽기/쓰기


for t in range(n * n - 1):  # 배열 모두 돌기, 달팽이 문제 무조건 이거 먼저 만들기
    cnt += 1
    ci, cj = ci + dx[dr], cj + dy[dr]
    pos.append((ci, cj))  # 2차원 달팽이 모양 -> 1차원 list로 변환
    # arr[ci][cj] = t + 1
    if cnt == cnt_max:
        cnt = 0
        dr = (dr + 1) % 4
        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_max += 1


def bomb(lst):
    global ans
    nlst = []  # 리턴에 사용
    lst.append(-1)
    i = 0
    while i < (len(lst) - 1):
        j = i + 1
        while lst[i] == lst[j]:
            j += 1
        if 4 <= (j - i):  # 폭발
            ans += lst[i] * (j - i)  # 구슬 번호 * 폭발 개수
        else:
            nlst += [lst[i]] * (j - i)
        i = j
    lst.pop()
    return nlst


ans = 0
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
# 0: 구슬 없는 칸
# 방향, 거리
for _ in range(c):
    d, s = map(int, input().split())
    # [1] d 방향으로 s만큼 뻗어가면서 arr을 0으로 변경 후 1차원 lst에 구슬 저장
    for mul in range(1, s + 1):
        arr[m + di[d] * mul][m + dj[d] * mul] = 0
    lst = []  # 0이 아닌 실제 구슬만 담기
    for i, j in pos:
        if arr[i][j] > 0:
            lst.append(arr[i][j])
    # [2] 연속 4개이상 폭팔시키고 더이상 폭발하지 않을 때까지 반복
    while True:
        # 4개이상 폭발(점수 추가), 나머지 반환
        tmp_list = bomb(lst)
        if len(tmp_list) == len(lst):
            # 더이상 폭발되지 않음
            break
        lst = tmp_list
    # [3-1] 구슬을 개수 + 번호로 변환
    lsta = []
    tmp_list.append(-1)  # 마지막 데이터 처리 위해서 패딩 (나중에 제거)
    i = 0
    while i < len(tmp_list) - 1:
        j = i + 1
        while tmp_list[i] == tmp_list[j]:  # 같을 동안 증가
            j += 1
        lsta += [(j - i), tmp_list[i]]
        i = j

    # [3-2] 1차원 -> 2차원 배열에 복사
    arr_new = [[0] * n for _ in range(n)]
    for i in range(0, min(len(lsta), len(pos))):
        arr_new[pos[i][0]][pos[i][1]] = lsta[i]
    arr = arr_new
print(ans)
