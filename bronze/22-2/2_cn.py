# 双指针

n = int(input())
a = list(map(int, input().split()))     # 原数组
b = list(map(int, input().split()))     # 目标数组

i = 0                # i是a的index
already = set()      # 记录已经左移的元素
for j in range(n):   # j是b的index
    while a[i] in already:     
        i += 1       # 如果a[i]是已经左移过的，则跳过（因为a[i]已经被左移走，不在当前位置了）
    if a[i] == b[j]:
        i += 1
    else:
        already.add(b[j])
print(len(already))