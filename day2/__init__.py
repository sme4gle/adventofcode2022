from typing import TypedDict

from common import read_input


def determine_score(a: str, b: str, second_objective: bool) -> int:
    '''
    Score is determined by the choice of item (Rock, Paper, Scissors).
    Rock equals a score of 1, Paper equals a score of 2, Scissors equals a score of 3.
    This score is given regardless a win or loss.
    For a win you gain an additional 6 points. For a draw you win 3 extra points.
    For a loss you gain no extra points except for the item choice.

    Objective 1:
    A/X = Rock
    B/Y = Paper
    C/Z = Scissors

    Objective 2:
    A = Rock
    B = Paper
    C = Scissors
    X = Lose
    Y = Draw
    Z = Win
    :param a:
    :param b:
    :param second_objective:
    :return:
    '''
    decypher_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    if not second_objective:
        res = decypher_dict[a] - decypher_dict[b]
        if res == 0:  # Draw
            return decypher_dict[b] + 3
        elif res in [-1, 2]:  # Win
            return decypher_dict[b] + 6
        else:  # Loss
            return decypher_dict[b]
    else:
        secondary_decypher_dict = {
            'A': 1,
            'B': 2,
            'C': 3,
        }

        if decypher_dict[b] == 1:  # Lose
            for key, value in secondary_decypher_dict.items():
                if secondary_decypher_dict[a] - value in [1, -2]:
                    return value
        elif decypher_dict[b] == 2:  # Draw
            for key, value in secondary_decypher_dict.items():
                if secondary_decypher_dict[a] - value == 0:
                    return value + 3
        else:  # Win
            for key, value in secondary_decypher_dict.items():
                if secondary_decypher_dict[a] - value in [-1, 2]:
                    return value + 6


if __name__ == '__main__':
    input = read_input()
    total_score = 0
    total_score_b = 0
    for game in input:
        a = game.split(' ')[0]
        b = game.split(' ')[1]
        # Challenge 1
        total_score += determine_score(a, b, False)

        # Challenge 2
        total_score_b += determine_score(a, b, True)

    print(total_score)
    print(total_score_b)
