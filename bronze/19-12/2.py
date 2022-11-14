# 字符串可以hash

# 这道题需要认真读题
# 说的是在当前K下，mailboxes不可重复

import sys
sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')

n = int(input())
colors = input()

for k in range(1, n+1):
    record = set()
    for j in range(n-k+1):
        mailboxes = colors[j:j+k]
        if mailboxes in record:
            break
        record.add(mailboxes)
    else:
        print(k)
        break