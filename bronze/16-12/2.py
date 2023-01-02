# word2中需要的那一个字母比word1中需要的多

import sys
sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

n = int(input())
words = []
for i in range(n):
    words.append(input().split())

# init alphabet
alphabet = dict()
for i in range(26):
    alphabet[chr(97+i)] = 0

# 统计word中每个字母的个数
def count_alphabet(word):
    tmp = dict()
    for i in word:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1
    return tmp

for word1,word2 in words:
    tmp1 = count_alphabet(word1)
    tmp2 = count_alphabet(word2)

    # 对于每一行，取所需blocks的最少数量
    # 独有的 -- 直接加
    # 共有的 -- 取大者
    for i in tmp1:
        if i not in tmp2:
            alphabet[i] += tmp1[i]
        else:
            alphabet[i] += max(tmp1[i], tmp2[i])

    for i in tmp2:
        if i not in tmp1:
            alphabet[i] += tmp2[i]
        # ps:别重复统计共有的

for v in alphabet.values():
    print(v)
