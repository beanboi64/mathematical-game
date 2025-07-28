# importing the random package to generate random numbers
import random
# printing the title of the game
print("***Mathematical Game***\n")
# asking the user to enter their name
user_name = input('Please enter your name: ')
# keep asking for the user's name if it's empty
while user_name == "":
    # prompt again for user's name
    user_name = input('Please enter your name: ')

# function to generate a random number between 0 and 100 (inclusive)
def num1_generator():
    # tuple list of numbers from 0 to 100
    number_set = tuple(range(0, 101))
    # randomly select and return one number from the tuple
    return random.choice(number_set)

# function to generate a random number between 0 and 100 (inclusive)
def num2_generator():
    # tuple list of numbers from 0 to 100
    number_set = tuple(range(0, 101))
    # randomly select and return one number from the tuple
    return random.choice(number_set)

# function to run the addition game
def addition():
    # initialize user's lives and score
    user_lives = 5
    user_score = 0
    # continue looping while user still has lives
    while user_lives > 0:
        # generate two random numbers
        num1 = num1_generator()
        num2 = num2_generator()
        # calculate the correct answer
        answer = num1 + num2
        # show the addition question to the user
        print(f"{num1} + {num2} = ")
        # get user's answer as an integer
        user_input = int(input('Enter your answer: '))
        # check if user's answer is incorrect
        if user_input != answer:
            # reduce user's lives by 1
            user_lives -= 1
            # display remaining lives and score
            print(f"Lives: {user_lives} Score: {user_score}")
            # show the correct answer
            print(f"Wrong! The correct answer was {answer}")
        else:
            # award 2 points for the correct answer
            user_score += 2
            # display remaining lives and updated score
            print(f"Lives: {user_lives} Score: {user_score}")
            # confirmation of correct answer
            print("Correct! Here's 2 points!")
        # if no lives remain, end the game
        if user_lives == 0:
            print("Whoops you're out of lives!")
            break
    # after game ends, congratulate or encourage user
    if user_score > 0:
        print(f"Congrats {user_name.capitalize()}! You scored {user_score} points")
    else:
        print(f"You need to hit them books {user_name.capitalize()}!")

# function to run the division game
def division():
    # initialize user's lives and score
    user_lives = 5
    user_score = 0
    # continue looping while user still has lives
    while user_lives > 0:
        # generate two random numbers
        num1 = num1_generator()
        num2 = num2_generator()
        # avoid division by zero by regenerating num2 if zero
        while num2 == 0:
            num2 = num2_generator()
        # calculate the division result
        answer = num1 / num2
        # round the answer to 2 decimal places for simplicity
        floatAnswer = round(answer, 2)
        # show the division question to the user
        print(f"{num1} / {num2} = ")
        # get user's answer as a float
        user_input = input('Enter your answer: ')
        user_input_float = float(user_input)
        # check if user's answer is incorrect
        if user_input_float != floatAnswer:
            # reduce user's lives by 1
            user_lives -= 1
            # display remaining lives and score
            print(f"Lives: {user_lives} Score: {user_score}")
            # show the correct rounded answer
            print(f"Incorrect the answer was {floatAnswer}")
        else:
            # award 2 points for the correct answer
            user_score += 2
            # display remaining lives and updated score
            print(f"Lives: {user_lives} Score: {user_score}")
            # confirmation of correct answer
            print("Correct! Here's 2 points!")
        # if no lives remain, end the game
        if user_lives == 0:
            print("GAME OVER! You're out of lives")
            break
    # after game ends, congratulate or encourage user
    if user_score > 0:
        print(f"Congrats {user_name.capitalize()}! You scored {user_score} points")
    else:
        print(f"You need to hit them books {user_name.capitalize()}!")

# function to run the multiplication game
def multiplication():
    # initialize user's lives and score
    user_lives = 5
    user_score = 0
    # continue looping while user still has lives
    while user_lives > 0:
        # generate two random numbers
        num1 = num1_generator()
        num2 = num2_generator()
        # calculate the multiplication result
        answer = num1 * num2
        # show the multiplication question to the user
        print(f"{num1} * {num2} = ")
        # get user's answer as an integer
        user_input = int(input('Enter your answer: '))
        # check if user's answer is incorrect
        if user_input != answer:
            # reduce user's lives by 1
            user_lives -= 1
            # show the correct answer
            print(f"Wrong! The correct answer was {answer}")
            # display remaining lives and score
            print(f"Lives: {user_lives} Score: {user_score}")
        else:
            # award 2 points for the correct answer
            user_score += 2
            # display remaining lives and updated score
            print(f"Lives: {user_lives} Score: {user_score}")
            # confirmation of correct answer
            print("Correct! Here's 2 points!")
        # if no lives remain, end the game
        if user_lives == 0:
            print("Whoops you're out of lives!")
            break
    # after game ends, congratulate or encourage user
    if user_score > 0:
        print(f"Congrats {user_name.capitalize()}! You scored {user_score} points")
    else:
        print(f"You need to hit them books {user_name.capitalize()}!")

# function to run the subtraction game
def subtraction():
    # initialize user's lives and score
    user_lives = 5
    user_score = 0
    # continue looping while user still has lives
    while user_lives > 0:
        # generate two random numbers
        num1 = num1_generator()
        num2 = num2_generator()
        # calculate the subtraction result
        answer = num1 - num2
        # show the subtraction question to the user
        print(f"{num1} - {num2} = ")
        # get user's answer as an integer
        user_input = int(input('Enter your answer: '))
        # check if user's answer is incorrect
        if user_input != answer:
            # reduce user's lives by 1
            user_lives -= 1
            # display remaining lives and score
            print(f"Lives: {user_lives} Score: {user_score}")
            # show the correct answer
            print(f"Wrong! The correct answer was {answer}")
        else:
            # award 2 points for the correct answer
            user_score += 2
            # display remaining lives and updated score
            print(f"Lives: {user_lives} Score: {user_score}")
            # confirmation of correct answer
            print("Correct! Here's 2 points!")
        # if no lives remain, end the game
        if user_lives == 0:
            print("Whoops you're out of lives!")
            break
    # after game ends, congratulate or encourage user
    if user_score > 0:
        print(f"Congrats {user_name.capitalize()}! You scored {user_score} points")
    else:
        print(f"You need to hit them books {user_name.capitalize()}!")

# defining menu options as variables
option1 = "1. Addition"
option2 = "2. Subtraction"
option3 = "3. Multiplication"
option4 = "4. Division"

# function to display the menu and handle user's choice
def game_menu():
    # show the menu options
    print(f"\n{option1}\n{option2}\n{option3}\n{option4}\n")
    # get the user's choice as an integer
    user_input = int(input('Enter your choice: '))
    # use conditional statements to call the corresponding function
    if user_input == 1:
        addition()
        # show the menu again after game ends
        game_menu()
    elif user_input == 2:
        subtraction()
        game_menu()
    elif user_input == 3:
        multiplication()
        game_menu()
    elif user_input == 4:
        division()
        game_menu()

# start the game by calling the menu
game_menu()
