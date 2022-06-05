import csv

file = open('espn.csv')


csvreader = csv.reader(file)
teams = {}
header = next(csvreader)
players = []
for player in csvreader:
    name = player[0]
    team = player[1]
    league = player[2]
    jersey = player[3]
    stats = player[4].split(",")
    position = stats[0]
    age = stats[1]
    height = stats[2]
    weight = stats[3]
    nation = stats[4]
    try:
        appearances = int(stats[5])
        if appearances > 15:
            point = [name, team, league, age, nation, position, jersey]
            players.append(point)
    except:
        ValueError
    
    # print(stats)
# print(players)

# next step is to create sqlite server and add players to it