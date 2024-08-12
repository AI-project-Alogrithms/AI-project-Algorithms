# 거짓말
# 교집합, 합집합
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
# 첫번째 수, 그 다음 사람 번호 (1~N)
tlst = set(map(int, input().split()[1:]))
# print(tlst) # 진실을 하는 사람
party = []
for _ in range(M): # 파티의 수 만큼 각 파티마다 오는 수와 번호가 같은 방식으로 주어짐
    tmp = set(map(int, input().split()[1:]))
    party.append(tmp)
# print(party)

for i in range(M): # 파티수만큼 돌동안
    for p in party: # 파티에 참석한 사람들이 진실을 알고 있는 사람과 있다면 그 사람도 진실을 알게됨
        if p & tlst:
            tlst = tlst.union(p)

cnt = 0
for p in party:
    if p & tlst: continue
    cnt +=1
print(cnt)





