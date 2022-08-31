# 不是什么操作都能合并在一个for循环里的
# guess[i] in d.keys()
# ''.join([ans1, ans2, ans3])
# 阅读理解


ans1 = input()
ans2 = input()
ans3 = input()

guess1 = input()
guess2 = input()
guess3 = input()

ans = ''.join([ans1, ans2, ans3])
guess = ''.join([guess1, guess2, guess3])

green = 0
yellow = 0

ansBreeds = set(ans)
guessBreeds = set(guess)

interact = ansBreeds.intersection(guessBreeds)
d = {}

# 正确breeds的数量
for i in range(len(ans)):
    if ans[i] in interact:
        if ans[i] in d.keys():
            d[ans[i]] += 1
        else:
            d[ans[i]] = 1

# 统计green
for i in range(len(ans)):
    if guess[i] == ans[i]:
        green += 1
        d[guess[i]] -= 1

# 统计yellow
for i in range(len(ans)):
    if guess[i] != ans[i] and guess[i] in interact \
            and guess[i] in d.keys() and d[guess[i]] > 0:
        yellow += 1
        d[guess[i]] -= 1

print(green)
print(yellow)


