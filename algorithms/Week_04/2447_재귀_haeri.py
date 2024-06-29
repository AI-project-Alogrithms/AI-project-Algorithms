import sys
sys.stdin=open("./Desktop/input.txt","r")
input = sys.stdin.readline

'''
재귀함수를 print로 찍을 수가 없을 것 같아서,
빈 이차원 리스트를 사전에 정의한 후 마지막에 print
'''

def f(x, y, step):    
    global board
    if step == 3: 
        board[x].append('***')
        board[x+1].append('* *')
        board[x+2].append('***')
        return
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: # 2행 2열인 경우 공백
                for t in range(int(step/3)):
                    board[x+i*int(step/3)+t].append(' '*int(step/3))
            else: # 그렇지 않은 경우
                f(x+i*int(step/3), y+j*int(step/3), int(step/3))

N = int(input())
board = [[] for _ in range(N)]
f(0, 0, N)

for i in range(len(board)):
    print(''.join(board[i]))