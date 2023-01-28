# word2中需要的那一个字母比word1中需要的多

import sys
sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

n = int(input())
words = []
for i in range(n):
    words.append(input().split())

ans = [0]*26

def count_alphabet(word):
    tmp = [0]*26
    for i in word:
        tmp[ord(i)-97] += 1
    return tmp

for word1,word2 in words:
    tmp1 = count_alphabet(word1)
    tmp2 = count_alphabet(word2)

    for i in range(26):
        # 两面的字母，取大者就行
        ans[i] += max(tmp1[i], tmp2[i])

for i in range(26):
    print(ans[i])
