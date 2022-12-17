from itertools import permutations
n = int(input())

cubes = []
for i in range(4):
    cubes.append(input())

words = []
ans = []
for i in range(n):
    words.append(input())
    ans.append(0)

for a in cubes[0]:
    for b in cubes[1]:
        for c in cubes[2]:
            for d in cubes[3]:
                blocks = a+b+c+d
                for order in permutations(blocks):
                    order = ''.join(order)
                    for j in range(len(words)):
                        if words[j] in order:
                            ans[j] = 1

for i in ans:
    if i == 1:
        print('YES')
    else:
        print('NO')