import sys
sys.stdin=open("./Desktop/input.txt","r")
input = sys.stdin.readline

from collections import defaultdict
# import numpy as np # ModuleNotFoundError 발생

count_dict = defaultdict(int)

def f(now_board):
    global count_dict # -1, 0, 1 의 개수를 담은 딕셔너리

    c = now_board[0][0]

    if len(now_board) == 1: # 1*1 행렬
        count_dict[c] += 1
        return
    
    flag = True
    # 모든 원소 값이 같은지 조사
    for i in range(len(now_board)):
        for j in range(len(now_board)):
            if now_board[i][j] != c:
                flag = False
                break
    
    step = int(len(now_board)/3) # 윈도우(?)의 크기

    if flag == False: # 원소 값 중 다른 게 있을 때: 행렬 9등분하여 다시 조사
        for i in range(3):
            for j in range(3):
                tmp = now_board[step*i:step*(i+1)]
                f([t[step*j:step*(j+1)] for t in tmp])
              #  f(now_board[step*i:step*(i+1),step*j:step*(j+1)]) # 2차원 배열 슬라이싱 - np.array(board) 일 때만 가능
        
    else: # 모든 원소의 값이 동일할 때
        count_dict[c] += 1
        return

N = int(input())
temp = N
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

f(board)
#f(np.array(board))
print(count_dict[-1])
print(count_dict[0])
print(count_dict[1])