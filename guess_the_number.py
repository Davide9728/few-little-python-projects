import random
selected_number = random.randint(0, 100)
flag = False #if number_selected is found, it sto the game
life = 0


choose_difficulty = input("choose difficulty, type 'hard' or 'easy': ") # set life
if choose_difficulty == 'hard':
    life = 5
else:
    life = 10

while flag != True:
    print(f"\nyou have {life} attempts to guess the number")

    if life == 0:
        flag = True
        print(f"you lost all life\ngame over\nthe answer was {selected_number}")

    else:
        player_num = int(input("guess the number"))
        if player_num == selected_number:
            print(f"you got it, the answer was {selected_number}")
            flag = True
        elif player_num < selected_number:
            print("too low")
            life -= 1
        elif player_num > selected_number:
            print("too high")
            life -= 1



