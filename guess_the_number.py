import random
number_selected = random.randint(0,100)
flag = False #if number_selected is found, it sto the game
life = 0


choose_difficulty = input("choose difficulty, type 'hard' or 'easy': ") # set life
if choose_difficulty == 'hard':
    life = 5
else:
    life = 10

while flag != True:

    if life == 0:
        flag = True
        print("you lost all life\ngame over")

    else:
        player_num = int(input("guess the number"))
        if player_num == number_selected:
            print("win")
            flag = True
        elif player_num < number_selected:
            print("too low")
            life -= 1
        elif player_num > number_selected:
            print("too high")
            life -= 1


print(f"numero random {number_selected}")
