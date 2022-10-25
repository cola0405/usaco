# closest to the day!
# not only next year
# it can be in the same year

n = int(input())

years = {}
name_animal = {}
animal_year = {'Ox':1, 'Tiger':2, 'Rabbit':3, 'Dragon':4, 'Snake':5,
     'Horse':6, 'Goat':7, 'Monkey':8, 'Rooster':9, 'Dog':10,
     'Pig':11, 'Rat':12}

years['Bessie'] = 1997
name_animal['Bessie'] = 'Ox'

for i in range(n):
    info = input().split()
    name1 = info[0]
    direction = info[3]
    animal = info[4]
    name2 = info[-1]
    name_animal[name1] = animal
    if direction == 'previous':
        years[name1] = years[name2] - (animal_year[name_animal[name2]] + 12 - animal_year[animal])
    else:
        years[name1] = years[name2] + (12 - animal_year[name_animal[name2]] + animal_year[animal])

print(years['Bessie'] - years['Elsie'])
