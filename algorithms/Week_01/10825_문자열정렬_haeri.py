
import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

N = int(input())
data_list = []
for _ in range(N):
    name, kuk, young, su = input().split()
    kuk, young, su = int(kuk), int(young), int(su)
    data_list.append([name, kuk, young, su])
    
sorted_list = sorted(data_list, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for data in sorted_list:
    print(data[0])