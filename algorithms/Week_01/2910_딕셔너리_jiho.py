import sys

input = sys.stdin.readline
n, c = map(int, input().split())
n_list = list(map(int, input().split()))
dict_n = {}
for i in n_list:
  try:
    dict_n[i] += 1
  except:
    dict_n[i] = 1
# print(dict_n)
dict_n = dict(sorted(dict_n.items(), key = lambda item: item[1], reverse=True))
# print(dict_n)
for key, value in dict_n.items():
  for _ in range(value):
    print(key, end =" ")
