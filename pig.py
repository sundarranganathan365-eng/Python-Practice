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

