
import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

N = int(input())
data_list = set() # 중복 제거를 위해
for _ in range(N):
    data_list.add(input().strip())
sorted_list = sorted(list(data_list), key=lambda x:(len(x), x)) # (단어 길이, 사전순)

for data in sorted_list:
    print(data)