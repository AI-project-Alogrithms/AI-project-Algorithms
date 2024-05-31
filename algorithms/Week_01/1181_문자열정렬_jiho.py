n = int(input())
dict_list = []
for i in range(n):
  dict_list.append(input())
# 길이가 짧은 것 부터
# 사전 순

dict_list = list(set(dict_list))
dict_list.sort()
dict_list.sort(key=lambda i:len(i))
for i in dict_list:
  print(i)