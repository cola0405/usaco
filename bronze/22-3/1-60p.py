# 60p 超时
# merge useless
# 重点在于怎么样不翻前面的
# 仅仅是影响下一位
# 只要方法统一，则不用担心顺序的问题
# 因为我们的终极目标是把所有的F变成T
# 拿超时的硬换去理解，其实就是在做这个
# 重点是处理flip的位置

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


def flip(i):
    while i >= 0:
        if marks[i] == '.':
            i -= 1
            continue
        marks[i] = not marks[i]
        i -= 1


ans = 0
i = len(marks) - 1
while i >= 0:
    if marks[i] == '.' or marks[i] == True:
        i -= 1
        continue
    ans += 1
    flip(i)
    i -= 1

print(ans)





