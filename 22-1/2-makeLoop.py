def sim():
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    # excellent code
                    lst = (a, b, c, d)
                    countCWinA = countCLoseToA = 0
                    countCWinB = countCLoseToB = 0
                    for i in lst:
                        for j in dieA:
                            if i > j:
                                countCWinA += 1
                            elif i < j:
                                countCLoseToA +=1
                        for k in dieB:
                            if i > k:
                                countCWinB += 1
                            elif i < k:
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





