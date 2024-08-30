# 전광판
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

numlst = {
    0: {(0, 1), (1, 0), (1, 2), (3, 0), (3, 2), (4, 1)},
    1: {(1,2),(3,2)},
    2: {(0,1),(1,2),(2,1),(3,0),(4,1)},
    3: {(0,1),(1,2),(2,1),(3,2),(4,1)},
    4: {(1,0),(1,2),(2,1),(3,2)},
    5: {(0,1),(1,0),(2,1),(3,2),(4,1)},
    6: {(0,1),(1,0),(2,1),(3,0),(3,2),(4,1)},
    7: {(0,1),(1,0),(1,2),(3,2)},
    8: {(0,1),(1,0),(1,2),(2,1),(3,0),(3,2),(4,1)},
    9: {(0,1),(1,0),(1,2),(2,1),(3,2),(4,1)}
}

n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()
    alst = list(map(int, a))
    blst = list(map(int, b))
    # print(alst, blst)
    if len(alst)<5:
        alst = [-1]*(5-len(alst)) + alst
    if len(blst)<5:
        blst = [-1]*(5-len(blst)) + blst
    # print(alst, blst)
    cnt = 0
    for i in range(5):
        if alst[i] == -1 and blst[i]==-1: continue
        if alst[i]==-1 and blst[i]!=-1:
            cnt+= len(numlst[blst[i]])
        elif alst[i]!=-1 and blst[i]==-1:
            cnt+= len(numlst[alst[i]])
        else:
            cnt+=(len(numlst[alst[i]] | numlst[blst[i]]) - len(numlst[alst[i]] & numlst[blst[i]]))
    print(cnt)
