
import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(input().strip())

def get_sum_of_int(x): # 문자열에서 숫자인 부분만 합을 계산하는 함수
    x = list(x)
    sum_of_int = 0
    for data in x:
        try:
            sum_of_int += int(data)
        except:
            pass
    return sum_of_int

data = sorted(data, key=lambda x:(len(x), get_sum_of_int(x), x)) # (단어의 길이, 정수의 합, 사전순정렬)

for x in data:
    print(x)