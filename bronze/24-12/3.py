from collections import defaultdict

def update_ans(seq):
    for seg in seq:
        if len(seg) == 3 and d[seg] >= f and seg[0] != seg[1] and seg[1] == seg[2]:
            ans.add(seg)
            
n,f = map(int, input().split())
s = input()

# count moo of beginnings
d = defaultdict(int)
for i in range(n-2):
    d[s[i:i+3]] += 1

ans = set()
update_ans(d)

for i in range(n):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c == s[i]: continue
        s1 = s[i-2:i] + c + s[i+1:i+3]
        add = []
        minus = []
        # only concern about the substrings near i
        for j in range(-2,1):
            seg = s[i+j: i+j+3]
            seg1 = s1[2+j: 2+j+3]
            d[seg] -= 1
            d[seg1] += 1
            add.append(seg)
            minus.append(seg1)
        update_ans(add + minus)
        
        # recover
        for seg in add: d[seg] += 1
        for seg in minus: d[seg] -= 1
        
print(len(ans))
for seg in sorted(ans):
    print(seg)