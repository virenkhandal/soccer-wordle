
positions_dict = {
                    'Attacker': ['ST', 'CF', 'RW', 'LW', 'RF', 'LF'], 
                    'Midfielder': ['CM', 'CAM', 'CDM', 'RM', 'LM'], 
                    'Defender': ['CB', 'RB', 'LB', 'LWB', 'RWB'],
                    'Goalkeeper': ['GK']
}

continent_dict = {
                    'North America': [],
                    'South America': [],
                    'Europe': [],
                    'Africa': [],
                    'Asia': [],
                    'Australia': []
}

def compare_team(answer, guess):
    true_team = answer.current_team()
    guess_team = guess.current_team()
    if guess_team == true_team:
        return 0
    elif guess_team in answer.get_teams():
        return 1
    else:
        return 2

def compare_league(answer, guess):
    true_league = answer.current_league()
    guess_league = guess.current_league()
    if guess_league == true_league:
        return 0
    elif guess_league in answer.get_leagues():
        return 1
    else:
        return 2

def compare_nationality(answer, guess):
    true_nationality = answer.get_nationality()
    guess_nationality = guess.get_nationality()
    if guess_nationality == true_nationality:
        return 0
    else:
        for key in continent_dict:
            if true_nationality in continent_dict[key]:
                if guess_nationality in continent_dict[key]:
                    return 1
        return 2

def compare_position(answer, guess):
    true_position = answer.get_position()
    guess_position = guess.get_position()
    if guess_position == true_position:
        return 0
    else:
        for key in positions_dict:
            if true_position in positions_dict[key]:
                if guess_position in positions_dict[key]:
                    return 1
        return 2

def compare_age(answer, guess):
    true_age = answer.get_age()
    guess_age = guess.get_age()
    if guess_age == true_age:
        return 0
    elif guess_age in range(true_age-2, true_age+2):
        return 1
    else:
        return 2

def compare_height(answer, guess):
    true_height = answer.get_height()
    guess_height = guess.get_height()
    if true_height == true_height:
        return 0
    elif guess_height in range(true_height - 2, true_height + 2):
        return 1
    else:
        return 2




