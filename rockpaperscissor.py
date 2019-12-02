import random

game=['paper','rock','scissor']
computer_win=0
player_win=0
computer=random.choice(game)
no_of_chances=random.randint(1,10)
totalgames=no_of_chances
player=input("Choose one from rock,paper or scissor")
while no_of_chances!=0:
    if computer==player:
        print("Both win")
        computer_win+=1
        player_win+=1
        no_of_chances-=1
    elif((computer=="rock" and player=="scissor")or
         (computer=="scissor" and player=="paper")or
         (computer=="paper" and player=="rock")):
         print("Computer wins")
         computer_win+=1
         no_of_chances-=1
    else:
        print("Player wins")
        player_win+=1
        no_of_chances-=1
    computer=random.choice(game)
    player=input("Choose one from rock,paper or scissor: ")
if(no_of_chances==0):
    print("*******Statistics:*********")
    print("Total games: ",totalgames)
    print("Computer wins total ",computer_win, " games")
    print("Player wins total ",player_win, " games")
