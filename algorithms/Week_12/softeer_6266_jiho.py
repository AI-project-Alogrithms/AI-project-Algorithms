import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 회의실은 9시부터 18시까지만 사용 가능
# 회의는 정확히 한 회의실을 연속한 일정 시간 동안만 점유(회의실,시작시간,종료시간)
# 회의의 시작과 종료 시각은 시간 단위로만 설정 가능
# 한 회의가 끝나는 시각에 다른 회의가 시작하는건 가능
# 길이가 0인 회의는 존재 X

# M개의 회의가 주어졌을 때
# 회의실 별로 비어있는 시간대를 출력
"""
먼저 각 회의실마다 예약 현황을 저장할 수 있는 1차원 배열을 선언(reser_dict[name] = [False]*19)
M개의 회의의 시작 시간과 종료 시간까지 1차원 배열을 예약 처리(reser_dict[name][i] = True)
9시부터 18시까지 순회하며 빈 시간대를 저장(timetable.append((start,end)))
"""
n, m = map(int, input().split())

name_list = sorted(list(input().rstrip() for _ in range(n)))

reser_dict = dict()

for name in name_list:
    reser_dict[name] = [False] * 19

for _ in range(m):
    name, start, end = input().split()

    start, end = int(start), int(end)

    for i in range(start, end):
        reser_dict[name][i] = True

for index, name in enumerate(name_list):
    print(f"Room {name}:")

    start, end = -1, -1

    timetable = []

    for i in range(9, 18):
        resered = reser_dict[name][i]
        if resered == False:
            if start == -1:
                start = i
                end = i + 1
            else:
                end = i + 1
        else:
            if end != -1:
                timetable.append((start, end))
                start, end = -1, -1
    if end != -1:
        timetable.append((start, end))

    if len(timetable) == 0:
        print("Not available")

    else:
        print(f"{len(timetable)} available:")
        for s, e in timetable:
            s = str(s).zfill(2)
            e = str(e).zfill(2)
            print(f"{s}-{e}")

    if index != (len(name_list) - 1):
        print("-----")