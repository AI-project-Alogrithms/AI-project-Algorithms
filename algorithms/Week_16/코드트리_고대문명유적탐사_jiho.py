# 삼성 SW 2024 오전 기출 => bfs, 시물레이션
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def add_bfs(arr):
    arr_copy = [a[:] for a in arr]
    # 각 인덱스 위치에서 탐색 시작
    v = [[0] * 5 for _ in range(5)]
    total_cnt = 0
    total_lst = []
    for ci in range(5):
        for cj in range(5):
            if v[ci][cj] == 0:
                lst, cnt =bfs(arr_copy, ci, cj, v, 2)
                total_lst += lst
                total_cnt += cnt

    for x, y in total_lst:
        arr_copy[x][y] = 0
    return arr_copy, total_cnt

def bfs(arr_copy, ci, cj, v, step): # 탐색
    # print("step: ", step)
    q = deque()
    q.append((ci,cj))
    v[ci][cj] = 1 # 방문 여부
    type = arr_copy[ci][cj]
    cnt = 1
    lst = [(ci, cj)]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and arr_copy[ni][nj]==type:
                v[ni][nj] = 1
                cnt+=1
                q.append((ni,nj))
                lst.append((ni,nj))
    if step==1:
        if cnt>=3:
            return cnt
        else:
            return 0
    else:
        if cnt >= 3:
            return lst, cnt
        else:
            return [], 0

def rotate_90(sub_arr):
    return list(map(list, zip(*sub_arr[::-1])))

def rotate_180(sub_arr):
    return [row[::-1] for row in sub_arr[::-1]]

def rotate_270(sub_arr):
    return list(map(list, zip(*sub_arr)))[::-1]

def selct_bfs(si, sj, sub_arr, num, step): # 배열에 다시 집어넣을 서브 배열과, 현재 회전 각도 저장
    # si, sj 위치부터 시작해서 서브배열로 배열 바꾸기
    arr_copy = [a[:] for a in arr]
    for i in range(3):
        arr_copy[si + i][sj:sj+3] = sub_arr[i]
    # for i in arr_copy:
    #     print(i)
    # 각 인덱스 위치에서 탐색 시작
    v = [[0] * 5 for _ in range(5)]
    total_cnt = 0
    total_lst = []
    for ci in range(5):
        for cj in range(5):
            if v[ci][cj] == 0:
                if step==1:
                    total_cnt+=bfs(arr_copy, ci, cj, v, step)
                else:
                    lst, _ =bfs(arr_copy, ci, cj, v, step)
                    total_lst+=lst

    if step==1:
        return total_cnt, num
    else:
        for x, y in total_lst:
            arr_copy[x][y] = 0
        return arr_copy, total_lst


def sub_arr_func(i,j, size, arr): # 3*3 배열 선택하기
    sub_arr = []
    for row in arr[i:i+size]:
        sub_arr.append(row[j:j+size])
    return sub_arr


K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
mlst = list(map(int, input().split()))
mq = deque(mlst)
ans = 0
while(K>0):
    # 3*3 선택 배열 추출
    sub_all_lst = []
    for i in range(3):
        for j in range(3):
            sub_clst = []
            sub_arr = sub_arr_func(i,j, 3, arr)
            # print("sub")
            # for s in sub_arr:
            #     print(s)
            # print(i,j)
            sub_arr90 = rotate_90(sub_arr) # 시계 방향 90도 회전
            cnt9, num = selct_bfs(i,j, sub_arr90, 90, 1) # arr 배열에 넣기 -> bfs 돌리기
            sub_clst.append((cnt9, num))
            sub_arr180 = rotate_180(sub_arr)  # 180도 회전
            cnt18, num = selct_bfs(i,j, sub_arr180, 180, 1) # arr 배열에 넣기 -> bfs 돌리기
            sub_clst.append((cnt18, num))
            sub_arr270 = rotate_270(sub_arr) # 270도 회전
            cnt27, num = selct_bfs(i,j, sub_arr270, 270, 1) # arr 배열에 넣기 -> bfs 돌리기
            sub_clst.append((cnt27, num))

            sub_clst.sort(key = lambda x: (-x[0], x[1]))
            # print(sub_clst)
            sub_all_lst.append((sub_clst[0][0], sub_clst[0][1], j+1, i+1)) # 그때의 cnt, 회전 각도 저장, 해당 서브 좌표 중심 열, 행,
    sub_all_lst.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))
    # print(sub_all_lst)
    final_select = sub_all_lst[0]
    # print(final_select)

    # 유물 획득 => step 2
    cnt, rotate, sj, si = final_select
    if cnt == 0: break # 유물이 발견되지 않았다면 탐사 종료
    ans += cnt
    sub_arr = sub_arr_func(si-1,sj-1, 3, arr)
    if rotate==90:
        sub_arr  = rotate_90(sub_arr)
    elif rotate==180:
        sub_arr = rotate_180(sub_arr)
    else:
        sub_arr = rotate_270(sub_arr)
    # 유물 지우기
    arr, total_lst = selct_bfs(si-1, sj-1, sub_arr, rotate, 2)

    # total_lst.sort(key=lambda x: (x[1],-x[0]))
    # 유물 다시 채우기 -> mlst (반복)
    while(True):
        # print("mq: ", mq)
        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j] == 0:
                    arr[i][j] = mq.popleft()
        arr, add_cnt = add_bfs(arr)
        if add_cnt == 0: break  # 더이상 유물이 발견되지 않는다면 졸료
        ans += add_cnt

    print(ans, end=" ")
    K-=1 # 한턴 끝
    ans = 0




