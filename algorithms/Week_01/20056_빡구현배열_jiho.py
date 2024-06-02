# 마법사 상어와 파이어볼
import sys

input = sys.stdin.readline

# nxn, 파이어볼 m개, 반복 k번
n, m, k = map(int, input().strip().split())  # 4, 2, 2

# 파이어볼 담을 통
fireball = []
for _ in range(m):
    r, c, m, s, d = map(int, input().strip().split())
    fireball.append((r - 1, c - 1, m, s, d))

# fireball = [(0, 0, 5, 2, 2), (0, 3, 7, 1, 6)]
# 한 행에 4개의 fireball 담을 공간 만들기
array = [[[] for i in range(n)] for i in range(n)]
# print(array)

# dx, dy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    while fireball:
        rf, cf, mf, sf, df = fireball.pop()
        # 위치 이동
        nx = (rf + dx[df] * sf) % n
        ny = (cf + dy[df] * sf) % n
        # print(nx, ny)
        array[nx][ny].append(
            [mf, sf, df]
        )  # 옮겨진 위치에 해당 파이어볼 질량, 속력, 방향 넣기
    # print(array)
    # print("fireball: ", fireball)
    for r in range(n):
        for c in range(n):
            if len(array[r][c]) >= 2:
                # print("두개 이상의 파이어볼이 있음")
                # 합치는 질량, 속력, 방향
                sum_m, sum_s = 0, 0
                sum_odd, sum_even = 0, 0
                lens = len(array[r][c])
                while len(array[r][c]) > 0:
                    m, s, d = array[r][c].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:  # 짝수이면
                        sum_even += 1
                    else:  # 홀수이면
                        sum_odd += 1
                if sum_even == lens or sum_odd == lens:  # 모두 짝수거나 모두 홀수이면
                    new_dir = [0, 2, 4, 6]
                else:
                    new_dir = [1, 3, 5, 7]
                # 4개의 파이어 볼 생성, 질량이 0이 안될때만
                if sum_m // 5 > 0:
                    for i in range(len(new_dir)):
                        fireball.append((r, c, sum_m // 5, sum_s // lens, new_dir[i]))
                    # print(fireball)

            elif len(array[r][c]) == 1:
                # print("한개 있음, 그래도 추가하기")
                fireball.append([r, c] + array[r][c].pop())
            # print(fireball)
sum = 0
for i in fireball:
    sum += i[2]
print(sum)
