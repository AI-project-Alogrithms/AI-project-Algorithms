import sys
input = sys.stdin.readline

def hanoi(N, start, end, aux):
    global count
    global answer
    if N == 1:
        answer.append([start, end])
        count += 1
        return
    hanoi(N-1, start, aux, end)
    count += 1
    answer.append([start, end])
    hanoi(N-1, aux, end, start)

count = 0
answer = []
N = int(input())
hanoi(N, 1, 3, 2)
print(count)
for ans in answer:
    print(' '.join(map(str, ans)))