# 题目给的范围会帮很多忙的！

lst = list(map(int, input().split()))
lst.sort()
a, b = lst[0], lst[1]
c = lst[-1] - a - b
print(a,b,c)


