table = input()
word = input()

ans = 0
i = 0
while i < len(word):
    for c in table:
        if i < len(word) and word[i] == c:
            i += 1
    ans += 1
print(ans)


