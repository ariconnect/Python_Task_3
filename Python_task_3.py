import random

def difficulty():
    print("Great let\'s get started")
    while True:
        level = input("Please start the game by typing Easy, Medium or Hard depending on your preferred level:")
        if level.lower() == "easy":
            random_choice = random.randrange(1, 11)
            guess_count = 6
            print("The answer is between 1 and 10 and you have 6 tries. Good luck!")
            result = [random_choice, guess_count]
            return result

        if level.lower() == "medium":
            random_choice = random.randrange(1, 21)
            guess_count = 4
            print("The answer is between 1 and 20 and you have 4 tries. Good luck!")
            result = [random_choice, guess_count]
            return result

        if level.lower() == "hard":
            random_choice = random.randrange(1, 51)
            guess_count = 3
            print("The answer is between 1 and 50 and you have 3 tries. Good luck!")
            result = [random_choice, guess_count]
            return result
        else:
            print("Invalid input- Please type Easy, Medium or Hard")
            True
win = []
loss = []
status = True
while status:
    result = difficulty()
    random_choice = result[0]
    guess_count = result[1]

    checking = True
    while checking:
        try:
            guess = input("Guess a number: ")
            if int(guess) is random_choice:
                print("You are right :)")
                print("Game Over")
                win.append(1)
                checking = False
                status = False

            elif int(guess) is not random_choice and guess_count > 1:
                guess_count -= 1
                print("Sorry, you are wrong and you have {} guess(es) remaining. Try again".format(guess_count))
                checking = True
            else:
                print("Game Over! the correct number was {}".format(random_choice))
                loss.append(1)
                checking = False
                status = False
        except ValueError:
            guess_count -= 1
            print("Only numbers are allowed in this game.You have {} guess(es) remaining. Try again".format(guess_count))

    else:
        another_game = input("Would you like to play another game:(Y/N)")
        if 'y' in another_game.lower():
            status = True
        else:
            print("Thanks for playing!You won {} time(s) and lost {} time(s)".format(sum(win), sum(loss)))
            exit()








