import sys

input = sys.stdin.readline

n = int(input())
list_n = []
for _ in range(n):
  age, name = input().rstrip().split()
  list_n.append((int(age), name))
# print(list_n)
# list_n = [(21, 'junkyu'), (21, 'dohyun'), (20, 'sunyoung')]

list_n = sorted(list_n, key = lambda x: x[0])
# print(list_n)
for i in list_n:
  print(" ".join(map(str, i)))
