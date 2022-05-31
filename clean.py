import csv

file = open('espn.csv')


csvreader = csv.reader(file)
teams = {}
header = next(csvreader)
players = []
for player in csvreader:
    name = player[0]
    team = player[1]
    jersey = player[2]
    stats = player[3].split(",")
    position = stats[0]
    age = stats[1]
    height = stats[2]
    weight = stats[3]
    nation = stats[4]
    try:
        appearances = int(stats[5])
    except:
        ValueError
    if appearances > 15:
        point = [name, team, age, nation, position, height, weight, jersey]
        print(point)
    # print(stats)

