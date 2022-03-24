from board import *

def guess(answer, guess, turn):
    player = compare_player(answer, guess)
    team = compare_team(answer, guess)
    league = compare_league(answer, guess)
    nationality = compare_nationality(answer, guess)
    position = compare_position(answer, guess)
    age = compare_age(answer, guess)
    height = compare_height(answer, guess)
    number = compare_number(answer, guess)
    scores = [player, team, league, nationality, position, age, height, number]
    color_board(scores, turn)
    turn += 1

def color_board(scores):
    pass



