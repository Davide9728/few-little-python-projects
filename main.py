from game_data import data
import random


def call_account(a_list):
    a_number_of_account = random.randint(0, len(a_list) -1)
    selected_account = data [a_number_of_account]
    data.remove(selected_account)
    return selected_account

def show_account(first, second):
    print("first account".upper())
    print(f"the name: {first['name']}\nthe description: {first['description']}\nthe country: {first['country']}\nnumber of follower: "
          f"{first['follower_count']} ")
    print("\nsecond account".upper())
    print(f"the name: {second['name']}\nthe description: {second['description']}\nthe country: {second['country']}")

def confronto(first, second, answer):
    state = ''
    if first['follower_count'] > second['follower_count']:
        state = 'low'
    else:
        state = 'high'
    if state == answer:
        return True
    else:
        return False


score = 0
game_over = False

first_account = call_account(data)


while game_over != True:
    print(f"your score {score}")
    second_account = call_account(data)
    show_account(first_account, second_account)
    utente = input("second account is to: HIGH or LOW")

    if confronto(first_account, second_account, utente):
            score += 1
            first_account = second_account
    else:
        print("game over")
        game_over = True








