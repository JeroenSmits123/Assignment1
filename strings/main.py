# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from mimetypes import guess_all_extensions


goal_player1 = "Ruud Gullit"
goal_player2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54
scorers = goal_player1 +" "+ str(goal_0)+", " + goal_player2 + " "+str(goal_1)
report = f'{goal_player1} scored in the {goal_0}nd minute \n{goal_player2} scored in the {goal_1}th minute'
print(report)