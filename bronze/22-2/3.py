# permutation

# when there exist two blocks available, we don't know choose which block is optimal
# so we need to try all possible orders
from itertools import permutations

def solve():
    word = input()
    for s in permutations(blocks, len(word)):  # try all possible orders
        for i in range(len(word)):
            if word[i] not in s[i]: break
        else:
            return True

n = int(input())
blocks = [input() for i in range(4)]

for _ in range(n):
    if solve(): print("YES")
    else: print("NO")
        
