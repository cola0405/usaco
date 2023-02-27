# 0.0060002803802490234
# 比3-1快了10倍


n = int(input())
#import time
#start = time.time()

cubes = []
for i in range(4):
    cubes.append(input())

words = []
ans = []
for i in range(n):
    words.append(input())
    ans.append(0)


def exist(word, blocks):
    for i in word:
        if i not in blocks:
            return False
        blocks.remove(i)
    return True

# build all combination
all_combination = []
for a in cubes[0]:
    for b in cubes[1]:
        for c in cubes[2]:
            for d in cubes[3]:
                cmb = [a,b,c,d]
                all_combination.append(cmb)

for cmb in all_combination:
    for i in range(len(words)):
        if exist(words[i], cmb):
            ans[i] = 1

for i in ans:
    if i == 1:
        print('YES')
    else:
        print('NO')

#print(time.time() - start)