# when there exist two blocks available, we don't know choose which block is optimal
# so we need to try all possible orders
from itertools import permutations

def ok():
    word = input()
    # s 是字符串数组，每个字符串就是一个block
    # 如:['ABCDEF', 'OOOOOO', 'UVWXYZ']
    # 这里就是把所有可能的排列都试一遍
    for s in permutations(blocks, len(word)):  
        for i in range(len(word)):
            if word[i] not in s[i]: break
        else:
            return True

n = int(input())
blocks = [input() for i in range(4)]

for _ in range(n):
    if ok(): print("YES")
    else: print("NO")
        
