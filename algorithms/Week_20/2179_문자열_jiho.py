# 비슷한 단어
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def common_func(str1, str2):
    min_len = min(len(str1), len(str2))
    # prefix = ""
    cnt = 0
    # 앞에서부터 비교
    for i in range(min_len):
        if str1[i]==str2[i]:
            # prefix+=str1[i]
            cnt+=1
        else:
            break
    return cnt

n = int(input())
lst = []
for i in range(n):
    lst.append((i,input().rstrip()))
# lst = [input().rstrip() for _ in range(n)]
# print(lst)
lst_sort = sorted(lst, key=lambda x: x[1])
max_len = 0
result = []
for i in range(n-1):
    for j in range(i+1, n):
        lens = common_func(lst_sort[i][1], lst_sort[j][1])
        # 더 긴 접두사 나오면 기존 결과 지우고 새로 추가
        if lens>max_len:
            max_len = lens
            result = [(lst_sort[i], lst_sort[j])]
        # 최대 길이와 같은 경우
        elif lens==max_len:
            result.append((lst_sort[i], lst_sort[j]))
# 입력 순서 기준 정렬
for i in range(len(result)):
    result[i] = sorted(result[i])

result.sort(key=lambda x: (x[0][0], x[1][0]))

# print(result)
print(result[0][0][1])
print(result[0][1][1])

