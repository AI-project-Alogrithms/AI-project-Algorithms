# 센서
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def func(lst, L):
    ans = 0
    cur_point = lst[0][0] # 맨 처음 시작 널판지 시작

    for start, end in lst: # 시작과 끝이 정해져 있음
        if cur_point > end:
            # 널판지로 해당 end까지 다 가렸다면
            continue
        elif cur_point<start: # 다음 웅덩이보다 현재 커서가 작다면 다음 웅덩이로 이동
            cur_point = start
        dist = end - cur_point # 거리 계산
        if dist % L == 0: # 다 붙였다면
            cnt = dist//L
        else: # 아니라면 한개가 더 필요
            cnt = dist//L + 1
        cur_point+= cnt*L # 현재 위치 업데이트
        ans+=cnt
    print(ans)




N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x: x[0])

func(lst, L)