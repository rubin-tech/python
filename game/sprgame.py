import random
def play():
    user = input("'r' for rock, 's' for scissor, 'p' for paper::: " )
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You won'

    return 'You lost'

def is_win(player, opponent):
    if (player =='r' and opponent == 's' ) or (player =='p' and opponent == 'r') or (player =='s' and opponent == 'p'):
        return True
    else:
        return False


print(play())