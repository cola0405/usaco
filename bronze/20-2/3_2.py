# 利用周期压缩k
# 同时注意不到一个周期的处理

# tuple 可hash，list不可hash
# 切片的坑[1:-1:-1]会输出空的数组

def reverse(start, end):
    start -= 1
    end -= 1
    for i in range((end-start)//2+1):
        cows[start+i], cows[end-i] = cows[end-i], cows[start+i]

import sys
sys.stdin = open("swap.in", "r")
sys.stdout = open("swap.out", "w")
n, k = map(int, input().strip().split())
a1, a2 = map(int, input().strip().split())
b1, b2 = map(int, input().strip().split())

cows = list(range(1, n + 1))
record = [tuple(cows)]
ans = []
for i in range(k):
    reverse(a1,a2)
    reverse(b1,b2)

    t = tuple(cows)
    if t == record[0]:
        cycle = len(record)
        ans = record[k % cycle]
        break
    else:
        record.append(t)
else:
    ans = record[-1]

for i in ans:
    print(i)



