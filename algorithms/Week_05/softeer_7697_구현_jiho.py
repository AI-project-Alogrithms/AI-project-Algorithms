# Phi Squared.. 안풀리는데 답도 없어서 정말 큰일임.. 포기ㅠ
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def die(lst):
    i=0
    copy_lst = [a[:] for a in lst]
    while(i<len(lst)):
       has_merged = False
       # print("i: ", i)
       for j in range(i-1, -1, -1):
           # print("i-1: ", j)
           if  lst[i][1] != 0 and lst[j][1] != 0 and lst[j][1] <= lst[i][1]:
               copy_lst[i][1] += copy_lst[j][1]
               copy_lst[j][1] = 0
               break
       for j in range(i+1, len(lst), 1):
           # print("i+1: ", j)
           if lst[i][1] != 0 and lst[j][1] != 0 and lst[j][1] <= lst[i][1]:
               copy_lst[i][1] += copy_lst[j][1]
               copy_lst[j][1] = 0
               break
       # print("list: ", lst)
       # print("copy_lst: ", copy_lst)
       i +=1
    new_lst = []
    for i in range(len(copy_lst)):
        if copy_lst[i][1] != 0:
            new_lst.append(copy_lst[i])
    # die(new_lst)
    return new_lst

N = int(input())
s = list(map(int, input().split()))
stack = []
for i in range(1,N+1):
    stack.append([i, s[i-1]])
# print(stack)
die(stack)
while(len(stack) > 1):
    new_stack = die(stack)
    stack = new_stack

print(stack[0][1])
print(stack[0][0])
