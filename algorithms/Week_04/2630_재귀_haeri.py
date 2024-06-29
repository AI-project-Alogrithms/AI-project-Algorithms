'''
1780번과 완전히 동일. 3->2로 숫자만 바꿔서 냄
'''

import sys
sys.stdin=open("./Desktop/input.txt","r")
input = sys.stdin.readline

from collections import defaultdict
#import numpy as np

count_dict = defaultdict(int)

def f(now_board):
    global count_dict
    
    c = now_board[0][0]
    
    if len(now_board) == 1:
        count_dict[c] += 1
        return
    
    flag = True
    for i in range(len(now_board)):
        for j in range(len(now_board)):
            if now_board[i][j] != c:
                flag = False
                break
    
    step = int(len(now_board)/2)
    if flag == False:
        for i in range(2):
            for j in range(2):
                tmp = now_board[step*i:step*(i+1)]
                f([t[step*j:step*(j+1)] for t in tmp])
              #  f(now_board[step*i:step*(i+1),step*j:step*(j+1)]) # np.array(board) 일 때만 가능
    else:
        count_dict[c] += 1
        return

N = int(input())
temp = N
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

f(board)
print(count_dict[0])
print(count_dict[1])