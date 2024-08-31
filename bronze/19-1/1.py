import sys
sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

def play(shell):
    count = 0
    for a,b,g in game:
        shell[a], shell[b] = shell[b], shell[a]
        if shell[g] == 1:
            count += 1
    return count

n = int(input())
game = [list(map(int, input().split())) for i in range(n)]
print(max(play([0,1,0,0]), play([0,0,1,0]), play([0,0,0,1])))