import sys
sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")

n = int(input())
games = []
for i in range(n):
    game = list(map(int, input().split()))
    games.append(game)

def play(rules):
    win1 = 0
    win2 = 0

    for i in range(n):
        p1,p2 = games[i]
        if p1 == p2:
            continue
        elif (p1 == rules[0] and p2 == rules[1]) \
            or (p1 == rules[1] and p2 == rules[2]) \
            or (p1 == rules[2] and p2 == rules[0]):
            win1 += 1
        else:
            win2 += 1
    return win1, win2

max_win = 0
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            rules = [a,b,c]
            if len(set(rules)) < 3:
                continue

            win1, win2 = play(rules)
            max_win = max(win1, win2, max_win)

print(max_win)



