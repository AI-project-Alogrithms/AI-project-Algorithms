# 경사로
import sys
from sys import stdin

# from collections import deque

# sys.stdin = open("Week_02/input.txt", "r")
input = sys.stdin.readline

# n, l
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 행 추출
# print(arr)

road_col = [[arr[j][i] for j in range(n)] for i in range(n)]  # 열 추출
# print(road_col)

row_real_check = [True] * n
col_real_check = [True] * n

# 경사로 세우는 배열 만들기
row_road_input = [[0] * n for _ in range(n)]
col_road_input = [[0] * n for _ in range(n)]


def check_road(arr, l, road_input, real_check):
    for ro in range(len(arr)):
        # road = arr[ro]
        value = arr[ro][0]
        cnt = 1
        for i in range(len(arr[ro])):
            # 한 로드 확인
            if value == arr[ro][i]:  # 같다면
                cnt += 1
                value = arr[ro][i]
            else:  # 같지 않다면
                if abs(value - arr[ro][i]) > 1:  # 차이가 1보다 크다면
                    real_check[ro] = False
                    break
                else:  # 차이가 1과 동일하다면
                    if value < arr[ro][i]:  # 작은 쪽이고, cnt가 l 길이만큼 있다면
                        if cnt < l:  # cnt가 작다면
                            real_check[ro] = False
                            break
                        else:
                            for ch in range(l, 0, -1):
                                # 경사로 세우기
                                if (
                                    i - ch < 0 or road_input[ro][i - ch] == 1
                                ):  # 범위 벗어남 또는 이미 경사로가 세워짐
                                    real_check[ro] = False
                                    break
                                else:  # 세워진 경사로가 없다면
                                    road_input[ro][i - ch] = 1
                            cnt = 1
                            value = arr[ro][i]

                    else:  # 큰쪽이라면 value > road[i]:
                        max_v = arr[ro][i]
                        cnt = 1
                        for ch in range(0, l):
                            if (
                                i + ch >= len(arr[ro]) or max_v != arr[ro][i + ch]
                            ):  # 범위 벗어남 또는 값이 일치하지 않음
                                real_check[ro] = False
                                break
                            cnt += 1
                        if cnt < l:  # 작은 쪽 개수가 l보다 작다면
                            real_check[ro] = False
                            break
                        else:  # 크다면
                            for ch in range(0, l, 1):
                                if (
                                    i + ch >= len(arr[ro]) or max_v != arr[ro][i + ch]
                                ):  # 범위 벗어남 또는 값이 일치하지 않음
                                    real_check[ro] = False
                                    break
                                else:  # 세워진 경사로가 없다면
                                    road_input[ro][i + ch] = 1
                            cnt = 1
                            value = arr[ro][i]


check_road(arr, l, row_road_input, row_real_check)
check_road(road_col, l, col_road_input, col_real_check)
# print(row_real_check)
# print(col_real_check)
count = 0
for i in range(len(row_real_check)):
    if row_real_check[i] is True:
        count += 1
    if col_real_check[i] is True:
        count += 1
print(count)
