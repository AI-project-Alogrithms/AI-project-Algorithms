import sys
input = sys.stdin.readline
s = list(input().strip())
# s= ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
s_list = []

for i in range(len(s)):
  s_list.append("".join(s[i:]))
s_list.sort()
print("\n".join(s_list))

