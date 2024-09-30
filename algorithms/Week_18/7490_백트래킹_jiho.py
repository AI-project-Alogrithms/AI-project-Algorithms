# 0 만들기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def remove_empty(lst):
    # print(lst)
    result = []
    tmp = '' # 공백 숫자 임시 저장
    for item in lst:
        if isinstance(item, int): # 숫자라면
            # 문자열로 변환해 이어 붙임
            tmp+= str(item)
        elif item==' ': # 공백인 경우 건너뜀
            continue
        else:
            if tmp: # 숫자를 이어 붙인 부분이 있으면 숫자로 변환
                result.append(int(tmp))
                tmp = ''
            result.append(item)
    if tmp:
        result.append(int(tmp)) # 마지막 숫자 넣기
    return result


def func(lst):
    # 공백 제거
    lst = remove_empty(lst)
    # print(lst)
    result = lst[0] # 첫번째 값을 초기값으로
    for i in range(1, len(lst)-1):
        oper = lst[i] # 연산자
        next_num = lst[i+1] # 다음 숫자
        if oper=='+': result+= next_num
        elif oper=='-': result-= next_num
        # else:
        #     result+=str(next_num)
        #     result.replace(' ','')
        #     result = int(result)
    # print(result)
    return result

def dfs(cnt, lst):
    if cnt==n:
        # print(lst)
        if func(lst)==0:
            print("".join(map(str, lst)))
        return
    for i in range(3):
        dfs(cnt+1, lst+[olst[i],cnt+1])
T = int(input())
olst = [' ','+','-']
for _ in range(T):
    n = int(input())
    dfs(1,[1])
    print()