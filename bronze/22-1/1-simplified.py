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
g = {}
for i in range(len(ans)):
    if ans[i] in interact:
        if ans[i] in d.keys():
            d[ans[i]] += 1
        else:
            d[ans[i]] = 1
    if guess[i] in g.keys():
        g[guess[i]] += 1
    else:
        g[guess[i]] = 1


for i in range(len(guess)):
    if guess[i] == ans[i]:
        green += 1
        d[ans[i]] -= 1

for i in range(len(guess)):
    if guess[i] != ans[i] \
            and guess[i] in interact:
        yellow += min(g[guess[i]], d[guess[i]])
        d[guess[i]] = 0


print(green)
print(yellow)