n = int(input())

table = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake","Horse",
         "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox"]
year = {"Bessie": 2500}

def get_animal(x):
    gap = abs(x - year["Bessie"])
    if x >= year["Bessie"]:
        return table[gap%12]
    else:
        return table[12 - gap%12]

for i in range(n):
    info = input().split()
    name1, name2 = info[0], info[-1]
    direction = info[3]
    animal = info[4]

    if direction == "previous":
        direction = -1
    else:
        direction = 1

    cur = year[name2] + direction
    while get_animal(cur) != animal:
        cur += direction
    year[name1] = cur

print(abs(year["Bessie"] - year["Elsie"]))








