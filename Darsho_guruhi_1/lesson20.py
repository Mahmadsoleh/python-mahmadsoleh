import random

top_of_range = input("Шумо як ракам гииред: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Шумо аз 0 болотар гиред')
        quit()
else:
    print("Шумо харф интихоб накунед")
    quit()

random_number = random.randint(0, top_of_range)
gueses = 0

while True:
    gueses +=1
    usrer_guess = input("Як ракам интихоб кунед: ")
    if usrer_guess.isdigit():
        usrer_guess = int(usrer_guess)
    else:
        print("Please tube a number!")
        continue
    if usrer_guess == random_number:
        print("Муборак бошад шумо ёфтед!")
        break
    elif usrer_guess > random_number:
        print("Шумо раками калон гирифтед")
    else:
        print("Шумо раками хурд гирифтен")
print("Шумо дар мудати",gueses, "бор ёфтед!" )
