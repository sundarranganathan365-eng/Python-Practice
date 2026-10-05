import random

def roll ():
    min_value = 1 
    max_value =2 
    roll = random.randint(min_value,max_value)
    return roll

while True :
    player = input("Enter the Number of Players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2<= player <= 4:
            break
        else :
            print('Enter 2 -4 Players max')
    else:
        print("Invalid, Input plz Try agian ")
    
max_score = 50 
player_score = [0 for _ in range(player)]
print(player_score)

while max(player_score) < max_score:
    print("\nPlayer number ",player_idx + 1 ,"turn has just started !\n")

    current_score = 0
    for player_idx in range(player):

        while True:
            should_roll = input('Would you like to roll (y): ')
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("you rolled a 1 ! Turn Done ")
                current_score = 0
                break
            else :
                current_score += value

                print("You rolled a : ",value)

            print("Your Current Score is :",current_score)
        player_score[player_idx] += current_score
        print("Your Total score is ",player_score[player_idx])




