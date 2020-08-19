from random import randint

turns = 0
correct_guess = 0


while turns < 3:
    
    number = randint(1,10)
    print(number)
    
    try:

        guess = int(input("Enter a number: "))

        if guess == number:
            print("Congratulations, you guessed correctly!")
            correct_guess += 1
            if correct_guess == 3:
                print("3 Correct guesses!")
            continue
        elif guess != number:
            print("Unfortunately, you guessed incorrectly!")
            turns +=1
            if turns == 3:
                while True:
                    answer = input("Would you like to continue (y/n): ").lower()
                    if answer == "yes" or answer == "y":
                        print("Okay, restarting the game!")
                        turns = 0
                        break
                    elif answer == "no" or answer == "n":
                        print("Thanks for playing!")
                        break
                    else:
                        print("Please enter 'Yes' or 'No'")
                        
    except ValueError as guess_catch:
        print("Incorrect value, please enter a number!")
