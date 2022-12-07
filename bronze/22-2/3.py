n = int(input())

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

for a in cubes[0]:
    for b in cubes[1]:
        for c in cubes[2]:
            for d in cubes[3]:
                blocks = list(a+b+c+d)
                for i in range(len(words)):
                    if exist(words[i], blocks):
                        ans[i] = 1

for i in ans:
    if i == 1:
        print('YES')
    else:
        print('NO')