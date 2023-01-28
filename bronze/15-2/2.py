import sys
sys.stdin = open("cow.in", "r")
sys.stdout = open("cow.out", "w")

n = int(input())
s = input()

c = 0
co = 0
cow = 0

for i in range(n):
    if s[i] == "C":
        c += 1
    elif s[i] == 'O':
        co += c
    else:
        cow += co

print(cow)
