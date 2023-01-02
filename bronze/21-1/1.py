table = input()
target = input()

ans = 0
heard = 0
while heard < len(target):
    for i in table:
        if heard < len(target) and target[heard] == i:
            heard += 1
    ans += 1

print(ans)


