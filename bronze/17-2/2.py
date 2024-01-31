# if a pair of cows(a,b) fit a_left < b_left < a_right < b_right
# then ans += 1

import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

log = input()
alphabet = [chr(i) for i in range(65,91)]
inx = {chr(i): [] for i in range(65,91)}
for i in range(52):
    inx[log[i]].append(i)

ans = 0
for i in range(26):     # permutation
    for j in range(26):
        a = alphabet[i]
        b = alphabet[j]

        a_left, a_right = inx[a]
        b_left, b_right = inx[b]

        if a_left < b_left < a_right < b_right:
            ans += 1
print(ans)