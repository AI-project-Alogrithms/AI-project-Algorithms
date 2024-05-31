import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

from collections import defaultdict
N = int(input())

data = defaultdict(int)
for _ in range(N):
    card = int(input())
    data[card] += 1
result = sorted(data.items(), key=lambda x:(-x[1], x[0])) # value(등장 횟수)가 큰 순, key(숫자 카드 넘버)는 작은 순에 따라 정렬
print(result[0][0])