# 字符串处理很棒的一道题
# 很多细节的地方要注意的


import sys
sys.stdin = open('word.in', 'r')
sys.stdout = open('word.out', 'w')

n, k = map(int, input().split())
words = input().split()

line = words[0]
chars = len(words[0])
for word in words[1:]:
    if chars + len(word) <= k:
        line = line + ' ' + word
        chars += len(word)
    else:
        print(line)
        line = word
        chars = len(word)
print(line)


