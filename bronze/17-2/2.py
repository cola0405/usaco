import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

log = input()

def get_index(target):
    inx = []
    for i in range(len(log)):
        if log[i] == target:
            inx.append(i)
    return inx[0], inx[1]

alphabet = []
path = dict()
for i in range(26):
    letter = chr(65+i)
    inx1, inx2 = get_index(letter)
    path[letter] = (inx1, inx2)
    alphabet.append(letter)

ans = 0
for i in range(26):
    for j in range(26):
        letter1 = alphabet[i]
        letter2 = alphabet[j]

        inx1, inx2 = path[letter1]
        inx3, inx4 = path[letter2]

        if inx1 < inx3 < inx2 < inx4:
            ans += 1

print(ans)


