"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = 'Sky'  # Change this line!


def final_strategy(score, opponent_score):
	bacon_gain = free_bacon(opponent_score)
    if bacon_gain >= GOAL_SCORE - score:
        return 0
    if score - opponent_score >= 25 and GOAL_SCORE - score <= 25:
        if bacon_gain >= cutoff:
            return 0
        else:
            return 2
    if extra_turn(score + bacon_gain, opponent_score):
        return 0
    return num_rolls

