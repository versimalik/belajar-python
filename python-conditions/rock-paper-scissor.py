from random import randint

print('Rock-Paper-Scissor Game')
print('=======================')

weapon = ['rock', 'paper', 'scissor']
computer = weapon[randint(0,2)]

print("What weapon do you want to use?")
print("Rock / Paper / Scissor")
player = input().lower()

if player == computer:
  print(f"Player and Computer use {player}")
  print("Nobody wins!")
elif player == 'rock':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'paper':
    print("Computer wins!")
    print("Paper covers Rock")
  elif computer == 'scissor':
    print("Player wins!")
    print("Rock smashes Scissor")
elif player == 'paper':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'rock':
    print("Player wins!")
    print("Paper covers Rock")
  elif computer == 'scissor':
    print("Computer wins!")
    print("Scissor cuts Paper")
elif player == 'scissor':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'rock':
    print("Computer wins!")
    print("Rock smashes Scissor")
  elif computer == 'paper':
    print("Player wins!")
    print("Scissor cuts Paper")
else:
  print("You input an invalid weapon!")