import sys
input = sys.stdin.readline
numbers = {}
for i in range(int(input())):
  key = int(input())
  if key not in numbers:
    numbers[key] = 0
  numbers[key] +=1
numbers = sorted(numbers.items(), key = lambda item: (-item[1], item[0]))
print(numbers[0][0])
