import sys
sys.stdin = open("reststops.in", "r")
sys.stdout = open("reststops.out", "w")

L,N,rf,rb = map(int, input().split())
rest = [tuple(map(int, input().split())) for _ in range(N)]
rest.sort(key=lambda item: item[0])
max_rest = max(rest, key=lambda item: item[1])

# 已经发现发现问题，如果后面有很大的val，则直接略过之前的，在后面休息多休息会！
# 是个贪心问题
# 然后休息完之后，后面还会有rest
# 那就是第二大问题，单调栈 -- 求它之后第二大的元素

# stack 保留递增序列,就是应该贪的顺序
stack = []
for i in range(N)[::-1]:
    pos,val = rest[i]
    if len(stack) == 0 or val > stack[-1][1]:
        stack.append(rest[i])
    if stack[-1] == max_rest:
        break

speed_diff = rf-rb
ans = 0
cur = 0
for i in range(len(stack))[::-1]:
    pos,val = stack[i]
    time_gap = (pos-cur)*speed_diff
    ans += time_gap*val
    cur = pos

print(ans)