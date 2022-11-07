# 100p

# 利用异或操作来判断是否flip
# 很cool

n = int(input())
s = input()


marks = []
i = 0
while i < len(s)-1:
    if s[i] == s[i+1]:
        marks.append(".")
    elif s[i+1] == 'G':
        marks.append(True)
    else:
        marks.append(False)
    i += 2

ans = 0
flag = False
i = len(marks) - 1
while i >= 0:
    if marks[i] == '.' or marks[i]^flag == True:
        i -= 1
        continue
    ans += 1
    flag = not flag
    i -= 1

print(ans)





