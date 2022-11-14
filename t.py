with open("highcard.in", "r") as reader:
    n = int(reader.readline().strip())
    card = [i for i in range(1, n * 2 + 1)]
    elsie = []
    bessie = []
    for _ in range(n):
        val = int(reader.readline().strip())
        elsie.append(val)
    elsie.sort()
    j = 0
    for i in range(len(card)):
        if card[i] != elsie[j]:
            bessie.append(card[i])
        elif j < len(elsie):
            j += 1
        if j == len(elsie):
            bessie.append(card[i])



def highcard(elsie, bessie, n):
    ans = 0
    elsie.sort(reverse=True)
    bessie.sort(reverse=True)
    for i in range(n - 1, -1, -1):
        if bessie[i] > elsie[len(elsie) - 1]:
            bessie.pop()
            elsie.pop()
            ans += 1
    return ans


with open("highcard.out", "w") as writer:
    writer.write(str(highcard(elsie, bessie, n)))