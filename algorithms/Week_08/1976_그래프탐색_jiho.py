# 여행가자 가고싶다~~
"""
union-find 알고리즘 이용하라는데 너무 이해가 어렵다...
처음 dfs => 메모리 초과
bfs로 이용하는 걸로 품 ==> 메모리 초과
"""
import sys
from sys import stdin
sys.setrecursionlimit(10**7)
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque


def union(x, y):
    # x와 y의 루트를 찾아 각각 x와 y에 저장합니다.
    x = find(x)
    y = find(y)
    # x와 y의 루트가 다르면, 두 트리를 합칩니다.
    # 항상 더 작은 값이 부모가 되도록 합니다.
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    # x의 루트를 찾는 함수입니다.
    if x != parents[x]:
        # 경로 압축을 통해 x의 부모를 재귀적으로 찾고, 부모를 루트로 설정합니다.
        parents[x] = find(parents[x])
    return parents[x]

# 도시의 수(n)와 여행 계획에 속한 도시들의 수(m)을 입력받습니다.
n, m = int(input()), int(input())
# 초기 부모를 자기 자신으로 설정하여 각 도시를 독립된 집합으로 만듭니다.
parents = [i for i in range(n)]
for i in range(n):
    # 각 도시의 연결 정보를 입력받습니다.
    link = list(map(int, input().split()))
    for j in range(n):
        # 연결 정보가 1인 경우, 두 도시를 같은 집합으로 합칩니다.
        if link[j] == 1:
            union(i, j)

# 경로 체크를 위해 parents 배열의 인덱스를 1부터 사용하기 위해 -1을 추가합니다.
parents = [-1] + parents
# 여행 계획을 입력받습니다.
path = list(map(int, input().split()))
# 여행 계획의 첫 도시의 부모를 찾습니다.
start = parents[path[0]]
# 여행 계획에 포함된 모든 도시가 동일한 집합에 속하는지 확인합니다.
for i in range(1, m):
    # 만약 어느 하나라도 부모가 다르다면, "NO"를 출력하고 종료합니다.
    if parents[path[i]] != start:
        print("NO")
        break
else:
    # 모든 도시가 같은 집합에 속한다면, "YES"를 출력합니다.
    print("YES")
