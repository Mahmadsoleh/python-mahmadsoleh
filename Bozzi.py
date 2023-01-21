import random

user_wins = 0
compyter_wins = 0

options = ["rock","paper","scisors"]

while True:
    user_input = input("Агар шумо нахохед бози кардан q нависед: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    compyter_pick=options[random_number]
    print("Compyter selekter: ", compyter_pick+'.')

    if user_input == "rock" and compyter_pick == "scisors":
        print("You win!")
        user_wins +=1
    elif user_input == "paper" and compyter_pick == "rock":
        print("You win!")
        user_wins +=1

    elif user_input == "scisores" and compyter_pick == "paper":
        print("You win!")
        user_wins +=1
    
    else:
        print("You lost!")
        compyter_wins +=1
print("You wan", user_wins, "times.")
print("compyter won", compyter_wins, "times.")
print("Good bye")