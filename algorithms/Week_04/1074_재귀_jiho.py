# z
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n,r,c = map(int, input().split())
def z(n,r,c,q):
    if n == 0:
        return (q)
    half = 2**(n-1) # 한 변의 절반의 길이
    if r < half:
        if c< half: # 1사분면
            quad = 1
        else: # 2사분면
            quad = 2
            c -= half
    else:
        if c<half:
            # 3사분면
            quad = 3
            r -= half
        else:
            quad = 4
            r -= half
            c -= half

    q +=(quad-1) * (half**2)
    return (z(n-1, r, c, q))
print(z(n,r,c,0))