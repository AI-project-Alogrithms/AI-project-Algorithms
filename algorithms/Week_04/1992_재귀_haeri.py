def solution(X, n): # 행렬 X, X는 n*n 행렬
    global answer
    t = X[0][0] # 같은지 다른지 판단할 기준 색상
    flag = True
    
    for i in range(n):
        for j in range(n):
            if X[i][j] != t:
                flag = False
                break
            
        if flag==False:
            break
    
    if flag:
        if t == 0: # 하얀색
            answer.append('0')
        
        else:
            answer.append('1')
            
    else:
        answer.append('(')
        A = list(map(list, zip(*list(map(list, zip(*X[0:int(n/2)])))[0:int(n/2)])))
        B = list(map(list, zip(*list(map(list, zip(*X[0:int(n/2)])))[int(n/2):])))
        C = list(map(list, zip(*list(map(list, zip(*X[int(n/2):])))[0:int(n/2)])))
        D = list(map(list, zip(*list(map(list, zip(*X[int(n/2):])))[int(n/2):])))
        solution(A, int(n/2))
        solution(B, int(n/2))
        solution(C, int(n/2))
        solution(D, int(n/2))
        answer.append(')')

        
answer = []

import sys
N = int(sys.stdin.readline()) # 1개

x = []
for _ in range(N):
    x.append(list(map(int, sys.stdin.readline().strip())))

solution(x, len(x))

print(''.join(answer))