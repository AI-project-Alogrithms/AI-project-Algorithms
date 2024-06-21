import sys
A, B, C = map(int, sys.stdin.readline().split()) # 2개


def solution(x,y,z):
    
    if y == 1:
        return x%z
    
    temp = solution(x, y//2, z)
    
    if y % 2 == 0:
        return temp* temp % z
    
    else:
        return temp* temp * x%z

print(solution(A, B, C) % C)