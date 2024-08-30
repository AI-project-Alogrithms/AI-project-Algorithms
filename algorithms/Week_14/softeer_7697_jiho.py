# phi squared => 큐 이용
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def func(cur_q,next_q): # 큐에 한개의 미생물만 남을 때까지 반복
    while len(cur_q)>1:
        while cur_q: # 한번의 반복 (하루 지나기)
            idx, cur_size = cur_q.popleft() # 현재 처리할 미생물
            tmp_size = 0 # 왼쪽, 오른쪽 살펴서 사이즈 추가하기 (기존 cur와 겹치게 하면 안되서 tmp 사용)
            if next_q and next_q[-1][1]<=cur_size: # 다음 일차의 마지막 번째가 현재 size보다 작거나 같으면
                next_idx, next_size = next_q.pop()
                tmp_size+= next_size
            if cur_q and cur_q[0][1]<=cur_size: # 오른쪽 위치가 현재 size보다 작거나 같으면
                right_idx, right_size = cur_q.popleft()
                tmp_size+= right_size
            cur_size+=tmp_size
            # 다음 일차에 업데이트 된 미생물 추가
            next_q.append((idx, cur_size))
        cur_q = next_q # 다음일차를 현재 일차로 변환
        next_q = deque() # 초기화
    return cur_q
# 큐의 시간 복잡도 => O(1)
N= int(input()) # 미생물의 개수

cur_q = deque() # 현재 일차에서 처리할 미생물
next_q = deque() # 다음 일차에서 처리할 미생물

# 초기 미생물 정보 입력 받기
lst = list(map(int, input().split()))
for i in range(N):
    cur_q.append((i+1, lst[i])) # (idx, 크기) 형태로 튜플로 저장

cur_q = func(cur_q,next_q)
ans_idx, ans_size = cur_q.popleft()
print(ans_size)
print(ans_idx)
