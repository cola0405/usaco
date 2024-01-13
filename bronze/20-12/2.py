# 模拟

ans = int(input())
flowers = list(map(int, input().split(" ")))

for i in range(len(flowers)):
    for j in range(i+1, len(flowers)):
        seg = flowers[i:j+1]
        average = sum(seg) / (j-i+1)
        if average in seg:
            ans += 1

print(ans)


