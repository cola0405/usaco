n, m = map(int, input().split())
s = input()
capacity = list(map(int, input().split()))

ans = sum(capacity)
for i in range(n):
    if s[i] == 'R' and s[(i+1)%n] == 'L':
        if s[i-1] == 'R':
            pre = 0
            j = i-1
            while s[j] == 'R':
                pre += capacity[j]
                j -= 1
            ans -= min(m, pre)
        if s[(i+2)%n] == 'L':
            pre = 0
            j = (i+2)%n
            while s[j%n] == 'L':
                pre += capacity[j]
                j = (j+1)%n
            ans -= min(m, pre)
print(ans)

'''
9 5
RRRLRRLLR
5 3 4 9 3 4 9 5 4
'''