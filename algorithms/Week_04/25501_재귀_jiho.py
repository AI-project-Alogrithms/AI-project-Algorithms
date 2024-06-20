# 재귀의 귀재
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt+1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

n = int(input()) # test case

for _ in range(n):
    s = input().rstrip()
    isi, cnt = isPalindrome(s)
    print(isi, cnt)