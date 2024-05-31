import sys
input=sys.stdin.readline

from collections import defaultdict

word = input().strip()
word_list = []
for i in range(len(word)):
    word_list.append(word[i:])

sorted_list = sorted(word_list)
for sorted_word in sorted_list:
    print(sorted_word)