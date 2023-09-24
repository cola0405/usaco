# 难点在于选取block的顺序
from itertools import permutations
n = int(input())
blocks = [input() for i in range(4)]

for _ in range(n):
    word = input()
    for selected_blocks in permutations(blocks, len(word)):  # 暴力尝试所有顺序
        selected_blocks = list(selected_blocks)
        for letter in word:
            for block in selected_blocks:
                if letter in block:
                    selected_blocks.remove(block)
                    break

            if len(selected_blocks) == 0:  # 被清空了则说明当前blocks序列可行
                print('YES')
                break
            else:
                print('NO')

                