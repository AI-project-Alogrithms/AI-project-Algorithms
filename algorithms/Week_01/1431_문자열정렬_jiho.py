import re
import sys
input = sys.stdin.readline
numbers = []
for i in range(int(input())):
  numbers.append(input().strip())
# print(numbers)

# numbers = ['ABCD', '145C', 'A', 'A910', 'Z321']

dict_n = {}
for i in numbers:
  if str.isalpha(i):
    dict_n[i] = 0
  else:
    # print(i)
    dict_n[i] = sum(list(map(int, list(re.sub(r'[^0-9]',"",i)))))
# print(dict_n)

dict_n = dict(sorted(dict_n.items(), key = lambda item: (len(item[0]), item[1], item[0])))
print("\n".join(dict_n.keys()))
                