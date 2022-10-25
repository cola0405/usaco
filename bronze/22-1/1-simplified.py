ans = ""
for i in range(3):
    ans += input()

guess = ""
for i in range(3):
    guess += input()

ansBreeds = set(ans)
guessBreeds = set(guess)
interact = ansBreeds.intersection(guessBreeds)

green = 0
yellow = 0


d = {}
for i in range(len(ans)):
    d[ans[i]] = 0
    if ans[i] in interact:
        if ans[i] in d.keys():
            d[ans[i]] += 1
        else:
            d[ans[i]] = 1

for i in range(len(guess)):
    if guess[i] == ans[i]:
        green += 1
        d[ans[i]] -= 1

for i in range(len(guess)):
    if guess[i] != ans[i] \
            and guess[i] in interact \
            and d[guess[i]] > 0:
        yellow += 1
        d[guess[i]] -= 1


print(green)
print(yellow)