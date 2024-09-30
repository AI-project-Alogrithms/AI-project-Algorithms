# 빗물
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import defaultdict
T = int(input()) # test case
for _ in range(T):
    word = input().rstrip()
    # print(word)
    k = int(input())

    # 알파벳 중 두개 이상 단어 찾기
    cnt_dict = defaultdict(int)
    for s in word:
        cnt_dict[s]+=1
    # print(cnt_dict)

    # 인덱스 저장
    idx_dict = defaultdict(list)
    alst = []
    for key, value in cnt_dict.items():
        if value>=k: # 2개 이상이라면
            alst.append(key)
    # print(alst)
    if len(alst)==0: # 만족하는 연속 문자열이 없다면
        print(-1)
        continue
    for a in alst:
        for idx, s in enumerate(word):
            if a==s:
                idx_dict[a].append(idx)
    # print(idx_dict)

    # k개가 들어갈때의 간격 저장
    anslst = []
    for key, value in idx_dict.items():
        for i in range(len(value)-k+1):
            anslst.append(value[i+k-1] - value[i])
    # print(anslst)
    print(min(anslst)+1, max(anslst)+1)

