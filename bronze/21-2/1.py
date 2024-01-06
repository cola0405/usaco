n = int(input())

year = {"Bessie": 12000}    # 足够大的year
table = ["Ox", "Tiger", "Rabbit", "Dragon",
            "Snake", "Horse", "Goat", "Monkey",
            "Rooster", "Dog", "Pig", "Rat"]  # 表示到左边Ox的距离

for i in range(n):
    info = input().split()
    name1, name2 = info[0], info[-1]
    direction, animal = info[3], info[4]
    cur = year[name2]

    while True:
        if direction == 'next':
            cur += 1
        else:
            cur -= 1
        if animal == table[cur%12]:     # 找到才停下
            year[name1] = cur
            break

print(abs(year['Bessie'] - year['Elsie']))

