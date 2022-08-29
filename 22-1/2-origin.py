
def sim():
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    countCWinA = 0
                    countCLoseToA = 0
                    countCWinB = 0
                    countCLoseToB = 0
                    for i in dieA:
                        if a > i:
                            countCWinA += 1
                        elif a < i:
                            countCLoseToA += 1
                        if b > i:
                            countCWinA += 1
                        elif b < i:
                            countCLoseToA += 1
                        if c > i:
                            countCWinA += 1
                        elif c < i:
                            countCLoseToA += 1
                        if d > i:
                            countCWinA += 1
                        elif d < i:
                            countCLoseToA += 1
                        # c lose
                    for i in dieB:
                        if a > i:
                            countCWinB += 1
                        elif a < i:
                            countCLoseToB += 1
                        if b > i:
                            countCWinB += 1
                        elif b < i:
                            countCLoseToB += 1
                        if c > i:
                            countCWinB += 1
                        elif c < i:
                            countCLoseToB += 1
                        if d > i:
                            countCWinB += 1
                        elif d < i:
                            countCLoseToB += 1

                    # C win A and C lose to B
                    if countCWinA > countCLoseToA and countCLoseToB > countCWinB:
                        print("yes")
                        return
    print("no")


n = int(input())

for line in range(n):
    die = list(map(int, input().split(" ")))
    dieA = die[:4]
    dieB = die[4:]

    # let A win B
    countAWin = 0
    countALose = 0
    for i in dieA:
        for j in dieB:
            if i > j:
                countAWin += 1
            elif i < j:
                countALose += 1

    # let A win B
    # Ps: can't just use "Awin > 8" as the condition, because there still got tie
    if countAWin < countALose:
        dieA, dieB = dieB, dieA
    sim()





