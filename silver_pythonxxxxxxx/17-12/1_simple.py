import sys
sys.stdin = open("homework.in", "r")
sys.stdout = open("homework.out", "w")

n = int(input())
scores = list(map(int, input().split()))

# 建表，用于之后高效求min
min_score = [0]*len(scores)
cur_min = float('inf')
for i in range(len(scores))[::-1]:
    cur_min = min(scores[i], cur_min)
    min_score[i] = cur_min

total = sum(scores)
max_avg_score = 0
avg_score = [0]*(len(scores)-2)
for i in range(len(scores)-2):
    total -= scores[i]
    cur_score = (total - scores[i] - min_score[i+1])/(len(scores)-2-i)
    avg_score[i] = cur_score

max_avg_score = max(avg_score)
for i in range(len(avg_score)):
    if avg_score[i] == max_avg_score:
        print(i+1)
