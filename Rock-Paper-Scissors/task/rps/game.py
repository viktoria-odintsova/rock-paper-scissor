import random

# identifying the name of the player
name = input("Enter your name:")
print("Hello, {}".format(name))
rating = open('rating.txt', 'r')

# identifying the starting rating score for the player
score = 0
for line in rating:
    input_name, input_points = line.split()
    if input_name == name:
        score = int(input_points)
rating.close()

# identifying the type of game the user want to play
options = input()
game_type = ""
if options == "":
    game_type = "traditional"
else:
    options = options.split(",")
print("Okay, let's start")

# playing the game until player decides to finish
while True:
    user_option = input()
    if user_option == "!exit":
        print("Bye!")
        break
    elif user_option == "!rating":
        print("Your rating: " + str(score))
    elif game_type == "traditional":
        rand_number = random.randint(1, 3)
        computer_choice = ""
        if rand_number == 1:
            computer_choice = "paper"
        elif rand_number == 2:
            computer_choice = "rock"
        elif rand_number == 3:
            computer_choice = "scissors"

        if user_option == computer_choice:
            print("There is a draw {}".format(computer_choice))
            score += 50
        elif user_option == "paper" and computer_choice == "rock" or user_option == "rock" and computer_choice == "scissors" or user_option == "scissors" and computer_choice == "paper":
            print("Well done. The computer chose {} and failed".format(computer_choice))
            score += 100
        elif user_option == "paper" and computer_choice == "scissors" or user_option == "rock" and computer_choice == "paper" or user_option == "scissors" and computer_choice == "rock":
            print("Sorry, but the computer chose {}".format(computer_choice))
        else:
            print("Invalid input")
    else:
        computer_choice = random.randint(0, len(options)-1)

        user_choice = options.index(user_option)
        if computer_choice == user_choice:
            print("There is a draw {}".format(user_option))
            score += 50
        elif user_option not in options:
            print("Invalid input")
        else:
            defeat_list = options[computer_choice+1:] + options[:computer_choice]
            user_choice = defeat_list.index(user_option)
            if user_choice + 1 <= len(defeat_list) // 2:
                print("Well done. The computer chose {} and failed".format(options[computer_choice]))
                score += 100
            else:
                print("Sorry, but the computer chose {}".format(options[computer_choice]))
