def check(d1, d2):
    countWin = countLose = 0
    for num1 in d1:
        for num2 in d2:
            if num1 > num2:
                countWin += 1
            elif num1 < num2:
                countLose += 1
    return countWin, countLose


def sim():
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    # excellent code
                    simDie = (a, b, c, d)
                    countCWinA, countCLoseToA = check(simDie, dieA)
                    countCWinB, countCLoseToB = check(simDie, dieB)

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
    # Ps: can't just use "Awin > 8" as the condition, because there got tie situation
    countAWinB, countALoseToB = check(dieA, dieB)
    if countAWinB < countALoseToB:
        dieA, dieB = dieB, dieA
    # 如果是平局的话，不用往下模拟了
    elif countAWinB == countALoseToB:
        print("no")
        continue
    sim()





