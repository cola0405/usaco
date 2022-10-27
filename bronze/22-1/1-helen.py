ans = ""
for i in range(3):
    ans += input()

guess = ""
for i in range(3):
    guess += input()


green = 0
yellow = 0

green_dict = {}
ans_dict = {}
error_dict = {}

for i in ans:
    green_dict[i] = 0
    ans_dict[i] = 0

for i in guess:
    error_dict[i] = 0

green = 0
for i in range(len(ans)):
    if ans[i] == guess[i]:
        green_dict[ans[i]] += 1
        green += 1
    else:
        error_dict[guess[i]] += 1
    ans_dict[ans[i]] += 1

yellow = 0
for i in guess:
    if i in ans and ans_dict[i] != -1:
        yellow += min(ans_dict[i] - green_dict[i], error_dict[i])
        ans_dict[i] = -1

print(green)
print(yellow)
