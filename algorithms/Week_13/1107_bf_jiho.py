# 1107 리모콘: 브로드포스 알고리즘
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from itertools import product


lst = list(map(int, input().rstrip()))
n = int(input())
blst = list(map(int, input().split()))

button = [0,1,2,3,4,5,6,7,8,9]# 버튼
initnum = 100 # 초기값

# 목표 채널 계산
target = int("".join(map(str, lst)))

# 초기 채널에서 +/-만으로 목표 채널로 이동할 경우
min_presses = abs(initnum - target)

# 고장나지 않은 버튼을 계산
usable_buttons = set(button) - set(blst)

# usable_buttons이 비어있으면 product가 아무 것도 반환하지 않으므로 확인 필요
if usable_buttons:
    # 목표 채널 길이의 조합 생성
    possible_nums = set(int(''.join(map(str, perm))) for perm in product(usable_buttons, repeat=len(lst)))

    # 목표 채널보다 한 자리 큰 숫자, 작은 숫자도 고려해야 함
    possible_nums.update(int(''.join(map(str, perm))) for perm in product(usable_buttons, repeat=len(lst) + 1))
    possible_nums.update(
        int(''.join(map(str, perm))) for perm in product(usable_buttons, repeat=len(lst) - 1) if len(lst) > 1)

    # 가능한 숫자 중 가장 가까운 숫자를 찾기
    for num in possible_nums:
        presses = abs(target - num) + len(str(num))
        min_presses = min(min_presses, presses)

print(min_presses)