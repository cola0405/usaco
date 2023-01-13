import sys

sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")

bronze1, bronze2 = map(int, input().split())
silver1, silver2 = map(int, input().split())
gold1, gold2 = map(int, input().split())
platinum1, platinum2 = map(int, input().split())

g2p = platinum2 - platinum1
s2g = gold2 - gold1 + g2p
b2s = silver2 - silver1 + s2g

print(b2s)
print(s2g)
print(g2p)


