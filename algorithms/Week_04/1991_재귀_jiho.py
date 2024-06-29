# 트리 순회
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def preorder(root):
    if root == ".": # 다시 돌아가기
        return
    print(root,end="")

    for i in range(1,len(tree)):
        if tree[i][0] == root:
            if tree[i][1] != ".":
                preorder(tree[i][1])

            if tree[i][2] != ".":
                preorder(tree[i][2])
            return

def inorder(root):
    if root == ".": # 다시 돌아가기
        return

    for i in range(1,len(tree)):
        if tree[i][0] == root:
            if tree[i][1] != ".": # left
                inorder(tree[i][1])
            print(root, end="")
            if tree[i][2] != ".": # rightl
                inorder(tree[i][2])
            return

def postorder(root):
    if root == ".": # 다시 돌아가기
        return

    for i in range(1,len(tree)):
        if tree[i][0] == root:
            if tree[i][1] != ".": # left
                postorder(tree[i][1])

            if tree[i][2] != ".": # rightl
                postorder(tree[i][2])
            print(root, end="")
            return

N = int(input())
tree = [[]]
for _ in range(N):
    arr = list(input().rstrip().split())
    tree.append(arr)
# print(tree)
# root left right
# n = 0
preorder(tree[1][0])
print()
inorder(tree[1][0])
print()
postorder(tree[1][0])