# 팰린드룸
import itertools
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from itertools import permutations

def is_palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    else:
        return False

T = int(input())

for _ in range(T):
    n = int(input())
    lst = []
    ans = 0
    for _ in range(n):
        lst.append(input().rstrip())
    perm = list(itertools.permutations(lst,2))
    # print(perm)
    for a, b in perm:
        if is_palindrome(a+b):
            ans = a+b
            break
    print(ans)



