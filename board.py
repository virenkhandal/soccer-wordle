import pycountry_convert as pc


positions_dict = {
                    'Attacker': ['ST', 'CF', 'RW', 'LW', 'RF', 'LF'], 
                    'Midfielder': ['CM', 'CAM', 'CDM', 'RM', 'LM'], 
                    'Defender': ['CB', 'RB', 'LB', 'LWB', 'RWB'],
                    'Goalkeeper': ['GK']
}

def compare_player(answer, guess):
    true_player = answer.get_name()
    guess_player = guess.get_name()
    return true_player == guess_player

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
    country_code = pc.country_name_to_country_alpha2(true_nationality, cn_name_format="default")
    true_continent_name = pc.country_alpha2_to_continent_code(country_code)
    guess_nationality = guess.get_nationality()
    country_code = pc.country_name_to_country_alpha2(guess_nationality, cn_name_format="default")
    guess_continent_name = pc.country_alpha2_to_continent_code(country_code)
    if guess_nationality == true_nationality:
        return 0
    elif true_continent_name == guess_continent_name:
        return 1
    else:
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
        return 0, None
    elif guess_age in range(true_age-2, true_age+2):
        if guess_age < true_age:
            return 1, "lower"
        else:
            return 1, "higher"
    else:
        if guess_age < true_age:
            return 2, "lower"
        else:
            return 2, "higher"

def compare_height(answer, guess):
    true_height = answer.get_height()
    guess_height = guess.get_height()
    if true_height == true_height:
        return 0, None
    elif guess_height in range(true_height - 2, true_height + 2):
        if guess_height < true_height:
            return 1, "lower"
        else:
            return 1, "higher"
    else:
        if guess_height < true_height:
            return 2, "lower"
        else:
            return 2, "higher"

def compare_number(answer, guess):
    true_number = answer.get_number()
    guess_number = guess.get_number()
    if guess_number == true_number:
        return 0, None
    elif guess_number in range(true_number-5, true_number+5):
        if guess_number < true_number:
            return 1, "lower"
        else:
            return 1, "higher"
    else:
        if guess_number < true_number:
            return 2, "lower"
        else:
            return 2, "higher"


