from random import*
import pygame

with open("words.txt", "r") as file:
    word_list = [word.strip() for word in file.readlines()]

solution = choice(word_list)

attempts = 7
display = ""
found_letters = ""

for l in solution:
    display = display + "_ "

print(">> Welcome to Hangman <<")

while attempts > 0:
    print("\nWord to guess: ", display)
    guess = input("Enter a letter: ")[0:1].lower()

    if guess in solution:
        found_letters = found_letters + guess
        print("-> Good guess!")
    else:
        attempts = attempts - 1
        print("-> Nope\n")
        if attempts == 0:
            print(" ==========Y= ")
        if attempts <= 1:
            print(" ||/ | ")
        if attempts <= 2:
            print(" || 0 ")
        if attempts <= 3:
            print(" || /|\ ")
        if attempts <= 4:
            print(" || /| ")
        if attempts <= 5:                    
            print("/|| ")
        if attempts <= 6:
            print("==============\n")

    display = ""
    for x in solution:
        if x in found_letters:
            display += x + " "
        else:
            display += "_ "

    if "_" not in display:
        print(">>> You win! <<<")
        break

print("\n * End of the game * ")