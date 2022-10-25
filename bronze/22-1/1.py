# 不是什么操作都能合并在一个for循环里的
# ps： 一定要先for处理green之后，才处理yellow
# 不然会鹊占鸠巢

# 阅读理解
# 品种正确，但是在错误的位置
# 要注意的是，正确的品种是有数量限制的

ans = ""
for i in range(3):
    ans += input()

guess = ""
for i in range(3):
    guess += input()

green = 0
yellow = 0

ansBreeds = set(ans)
guessBreeds = set(guess)

interact = ansBreeds.intersection(guessBreeds)
# ans中各品种的总数量
d = {}

# 在ans中寻找各品种的总数量
for i in range(len(ans)):
    if ans[i] in interact:
        if ans[i] in d.keys():
            d[ans[i]] += 1
        else:
            d[ans[i]] = 1

# 统计green
# ps： 一定要先for处理green之后，才处理yellow
# 不然会鹊占鸠巢
for i in range(len(guess)):
    if guess[i] == ans[i]:
        green += 1
        # 剩余品种正确的个数
        d[guess[i]] -= 1

# 统计yellow
for i in range(len(guess)):
    # 品种正确，但是在错误的位置
    # 要注意的是，正确的品种是有数量限制的
    if guess[i] != ans[i] \
            and guess[i] in interact \
            and d[guess[i]] > 0:
        yellow += 1
        # 剩余品种正确的个数
        d[guess[i]] -= 1

print(green)
print(yellow)


