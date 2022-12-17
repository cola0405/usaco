# 枚举不出来的
# 因为没办法通过遍历去进行淘汰

# 题目看似是找正确的提问序列
# 其实可以把问题进行转换
# 找的其实是一对，最相似的一对1

# 集合intersection


import sys
sys.stdin = open("guess.in", "r")
sys.stdout = open("guess.out", "w")

count = dict()
animal_chas = dict()
n = int(input())

for i in range(n):
    line = input().split()
    animal = line[0]
    chas = line[2:]
    animal_chas[animal] = set(chas)

count = 0
pair = ()
for i in animal_chas:
    for j in animal_chas:
        if i == j:
            continue
        intersect_num = len(animal_chas[i] & animal_chas[j])
        count = max(count, intersect_num)

print(count+1)






