import sys

a = [1,2,3]
b = [1,2,3]

d = {'a':[1,2],'b':[1,2]}

ans = 0
for a in range(2):
    for b in range(2):
        # 奇+奇
        # 1 1
        if (a+b)%2 == 0:
            # d['a'][1] * d['b'][1]
            ans += d['a'][a] * d['b'][b]
print(ans)


