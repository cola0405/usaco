# 字符串可以hash

# 这道题需要认真读题
# 说的是在当前K下，mailboxes不可重复

import sys
sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')

n = int(input())
mailbox = input()

for k in range(1,n+1):
    s = set()
    for i in range(n-k+1):
        sequence = mailbox[i:i+k]
        if sequence in s:
            break
        s.add(sequence)
    else:
        print(k)
        break