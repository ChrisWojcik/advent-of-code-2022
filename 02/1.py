import sys

rounds = []

for line in sys.stdin:
  line = line.strip()
  [oponent, me] = line.split(' ')
  
  decrypted = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
  }

  rounds.append([decrypted[oponent], decrypted[me]])

def rock_paper_scissors(player1, player2):
  WIN = 6
  DRAW = 3
  LOSS = 0

  SCORES = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
  }

  if player1 == player2:
    return DRAW + SCORES[player1]
  elif (player1 == 'ROCK'     and player2 == 'SCISSORS') or \
       (player1 == 'PAPER'    and player2 == 'ROCK') or \
       (player1 == 'SCISSORS' and player2 == 'PAPER'):

    return WIN + SCORES[player1]
  else:
    return LOSS + SCORES[player1]

total_score = 0

for round in rounds:
  [oponent, me] = round

  total_score += rock_paper_scissors(me, oponent)

print(total_score)
