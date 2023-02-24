# 根据题目给的关系公式递推求解
import sys
sys.stdin = open('photo.in', 'r')
sys.stdout = open('photo.out', 'w')
n = int(input())
b = list(map(int, input().split()))

# 枚举数字
# 牛的编号是1到n，不重复
for i in range(1, n+1):
    j = 0
    ans = [str(i)]
    temp_a = i
    while temp_a > 0 and j < len(b):
        temp_a = b[j] - temp_a
        ans.append(str(temp_a))
        j += 1
    s = set(ans)
    if len(s) == len(ans) and j == len(b):
        print(' '.join(ans))

