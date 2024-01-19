# 贪心 + 论证

# 很关键的一个思路 —— 有一些步骤是必须进行的，那我们可以从左往右处理
# 接着要思考的一个点，是否要为了之后的升而委屈中间的 —— 结论是不需要！
# 因为委屈了n个单位，之后也需要必须的指令补上这n个单位
# 所以，只贪能够顺带处理的就可以了，这就是最优解 —— 因为每一步操作都是必须的

# 相关优化：把两个研究对象转换成一个diff
# 同方向的就顺带，然后看是否需要额外操作
# 不同方向的，不可能顺带 —— 有多余的损耗，肯定不会是最优解

n = int(input())
target = list(map(int, input().split(" ")))
origin = list(map(int, input().split(" ")))
diff = [target[i]-origin[i] for i in range(n)]

ans = abs(diff[0])
for i in range(1, len(diff)):
    if diff[i]*diff[i-1] > 0:   # 同调
        ans += max(0, abs(diff[i]) - abs(diff[i-1]))    # abs之差<0表示可以顺带调整到位，abs之差>0表示需要额外操作
    else:
        ans += abs(diff[i])     # 方向性则不可能顺带

print(ans)
