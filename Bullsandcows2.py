
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Veronika Pindíková
email: veronika.pindikova@gmail.com
discord: Veronika77
"""
import random
import time
import csv
def generate_unique_secret_number():
    digits = list(range(1, 10))
    random.shuffle(digits)
    secret_number = "".join(map(str, digits[:4]))
    return secret_number

def validate_user_input(guessed_number, previous_guesses):
    if not guessed_number.isdigit():
        print("Warning: Please enter a valid number.")
        return False
    elif len(guessed_number) != 4:
        print("Warning: The number must have exactly 4 digits.")
        return False
    elif len(set(guessed_number)) != 4:
        print("Warning: Digits should not be repeated in your guess.")
        return False
    elif guessed_number.startswith("0"):
        print("Warning: The number should not start with zero.")
        return False
    elif guessed_number in previous_guesses:
        print("Warning: You have already guessed this number. Please choose a different number for your guess.")
        return False
    return True

def print_bulls_and_cows(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")

def guess_numbers():
    guessed_numbers = set()
    secret_number = generate_unique_secret_number()
    print(f"Secret number: {secret_number}")
    start_time = time.time()
    attempts = 0
    print("Hi there!")
    print("-"*45)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print("-"*45)
    while True:
        guessed_number = input("Enter your guess: ")
        if validate_user_input(guessed_number, guessed_numbers):
            guessed_numbers.add(guessed_number)
            bulls, cows = 0, 0
            for i in range(4):
                if guessed_number[i] == secret_number[i]:
                    bulls += 1
                elif guessed_number[i] in secret_number:
                    cows += 1
            print_bulls_and_cows(bulls, cows)
            attempts += 1
            if bulls == 4:
                end_time = time.time()
                if 1 <= (attempts) <= 3:
                    print(f"Congratulations! That´s amazing! You've guessed the secret number in {attempts} attempts!\nTotal time taken: {end_time - start_time:.2f} seconds.")
                elif 4 <= (attempts) <= 10:
                    print(f"Congratulations! That´s very good! You've guessed the secret number in {attempts} attempts!\nTotal time taken: {end_time - start_time:.2f} seconds.")  
                else:                 
                    print(f"Congratulations! You guessed the secret number in {attempts} attempts!\nTotal time taken: {end_time - start_time:.2f} seconds.")                      
                with open("game_stats.csv", "a", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([attempts, end_time - start_time])
                with open("game_stats.csv", "r" ) as csvfile:
                        writer = csv.reader(csvfile)
                        for line in writer:
                            print(line) 
                
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != "y":
                 break

guess_numbers() 
