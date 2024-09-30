# 센서
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 그리디
n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()
# print(lst)
idx_lst = []
for i in range(n-1):
    idx_lst.append(lst[i+1]-lst[i])
# 수신 가능 영역이 가장 긴 구간을 찾아서 그 구간을 제외시키고 k번째 수신기를 넣으면 된다
# 즉, 구간이 긴 부분은 연결하지 않는 것임. 그렇게 하면 최소 길이로 수신기 길이를 구할 수 있음
# 구간이 긴 부분들간은 길이가 0이기 때문
idx_lst.sort(reverse=True)
# print(idx_lst)
print(sum(idx_lst[k-1:]))