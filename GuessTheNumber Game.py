import random


def guess_the_number():
    print("Welcome to GuessTheNumber game, choose the difficulty ")
    print("1 - Easy   2 - Medium  3 - Hard  4 - Impossible ")
    difficulty = int(input())

    if difficulty == 1:
        number_of_tries = 3
        number_to_find = random.randint(1, 6)
        while number_of_tries != 0:
            print(f"You have {number_of_tries} tries, choose between 1 to 6")
            chosen_number = int(input("your number is?:"))
            if chosen_number == number_to_find:
                print("Chosen number is correct, you win!")
                print("Wanna play again? 1 - Yes  2 - No:")
                reset = int(input())
                if reset == 1:
                    guess_the_number()
                else:
                    print("Goodbye!")
                    exit()

    if difficulty == 2:
        number_of_tries = 3
        number_to_find = random.randint(1, 11)
        while number_of_tries != 0:
            print(f"You have {number_of_tries} tries, choose between 1 to 11")
            chosen_number = int(input("your number is?:"))
            if chosen_number == number_to_find:
                print("Chosen number is correct, you win!")
                print("Wanna play again? 1 - Yes  2 - No:")
                reset = int(input())
                if reset == 1:
                    guess_the_number()
                else:
                    print("Goodbye!")
                    exit()

    if difficulty == 3:
        number_of_tries = 3
        number_to_find = random.randint(1, 16)
        while number_of_tries != 0:
            print(f"You have {number_of_tries} tries, choose between 1 to 15")
            chosen_number = int(input("your number is?:"))
            if chosen_number == number_to_find:
                print("Chosen number is correct, you win!")
                print("Wanna play again? 1 - Yes  2 - No:")
                reset = int(input())
                if reset == 1:
                    guess_the_number()
                else:
                    print("Goodbye!")
                    exit()

    if difficulty == 4:
        number_of_tries = 3
        number_to_find = random.randint(1, 21)
        while number_of_tries != 0:
            print(f"You have {number_of_tries} tries, choose between 1 to 20")
            chosen_number = int(input("your number is?:"))
            if chosen_number == number_to_find:
                print("Chosen number is correct, you win!")
                print("Wanna play again? 1 - Yes  2 - No:")
                reset = int(input())
                if reset == 1:
                    guess_the_number()
                else:
                    print("Goodbye!")
                    exit()

            print("Entered number is incorrect, choose another")
            number_of_tries -= 1

        print("Oops, it seems that you loose, wanna play again? ")
        print("1 - Yes  2- No")
        again = int(input())
        if again == 1:
            guess_the_number()
        else:
            print("Goodbye!")
            exit()


print("Hello mate, wanna play a Guess the number game?")
print("1 - Yes   2 - No")
while True:
    choose_to_play = int(input())
    if choose_to_play == 2:
        print("Bye, see you another time!")
        exit()
    if choose_to_play == 1:
        guess_the_number()
    else:
        print("Wrong number, Type another")
