# 이차원 배열과 연산
import sys
from sys import stdin

sys.stdin = open("algorithms/input.txt", "r")

input = sys.stdin.readline
from collections import defaultdict

# A[r][c] == k
r, c, k = map(int, input().split())
r = r - 1
c = c - 1
arr = [list(map(int, input().split())) for _ in range(3)]

cnt = 0


def make_sort(arr):
    max_col = 0

    # 행 기준 정렬
    new_arr = []
    for row in arr:
        i_dict = defaultdict(int)
        # 한 행씩 딕셔너리에 담아서 (key, value) 로 만들기 count
        for key in row:
            if key != 0:
                i_dict[key] += 1
        # print(i_dict)
        # if 0 in i_dict:  # 0 이 있다면 제거
        #     i_dict.pop(0)
        # print(i_dict)
        new_row = list(sorted(i_dict.items(), key=lambda x: (x[1], x[0])))

        for i in range(len(new_row)):
            new_row[i] = list(new_row[i])
            # print(i)
        # 새로운 행 만들기
        new_arr.append(sum(new_row, []))
    # print(new_arr)

    for i in range(len(new_arr)):
        max_col = max(max_col, len(new_arr[i]))
    # print(max_col)
    for i in new_arr:
        i += [0] * (max_col - len(i))  # 가장 긴 길이에 맞춰서 0 추가
        if len(i) > 100:
            i = i[:100]
    return new_arr


while True:
    if cnt > 100:  # 만약 100초가 지났다면
        cnt = -1
        break
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
        break
    else:
        cnt += 1
        if len(arr) >= len(arr[0]):
            # 행기준 정렬
            arr = make_sort(arr)
            # print("row arr: ", arr)

        else:
            # 열기준 정렬
            arr = list(zip(*arr))
            # arr = [[arr[j][i] if j < /len(arr) and i < len(arr[j]) else 0 for j in range(max_row)] for i in range(max_col)]
            # print(arr)
            for i in range(len(arr)):
                arr[i] = list(arr[i])
            arr = make_sort(arr)
            # 다시 행 기준으로 변환
            arr = list(
                zip(*arr)
            )  # arr = [[arr[j][i] for j in range(max_row)] for i in range(max_col)]
            for i in range(len(arr)):
                arr[i] = list(arr[i])
print(cnt)
