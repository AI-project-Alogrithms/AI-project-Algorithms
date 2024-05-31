import sys
input = sys.stdin.readline
nums = list(map(int, input().split()))
count = nums[0]
vocab = nums[1:]
i = len(vocab)
while(i<count):
  add_vocab = list(map(int, input().split()))
  i += len(add_vocab)
  vocab += add_vocab
# print(vocab)

# vocab = [5, 2233, 1601, 90100, 13009, 802, 5000000, 301, 7654321, 210]
reverse_voc = []
for i in vocab:
  # 문자열 역순 출력
  reverse_voc.append(int(str(i)[::-1]))
reverse_voc.sort()
print('\n'.join(map(str, reverse_voc)))