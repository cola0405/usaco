# 先手写
# 小的有严格限制，所以从小的开始
# 小的放了，到下一个棚能放的种类自然是-1
# 再下一个棚则是-2

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

nums = []
for i in b:
    count = 0
    for j in a:
        if j <= i:
            count += 1
    nums.append(count)

ans = 1
step = 0
for i in nums:
    ans *= i-step
    step += 1

print(ans)