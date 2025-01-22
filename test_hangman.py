import random

words = ["concern", "window", "settlement", "sunshine", "retain", "constellation", "finance"
        "safari","philosophy","follow","cotton","rabbit","energy","identity","season"]

with open("words.txt","w") as file:
    for word in words:
        file.write(word + "\n")

#print("Menu")
#print("Play  == 1 ")
#print("Insert a new word == 2")

#choose a words ramdomly
def words_ramdom(file):
    with open (file, 'r') as f:
        words = f.read().splitlines()
    return(random.choice(words))
 
#for put the underscore 
def convert_pendu(word, found_letters):
    return ' '.join([letter if letter in found_letters else "_" for letter in word])
#beggining of a hangman
def hangman():
    word = words_ramdom("words.txt")
    found_letters = set()
    try_remaining = 6
    print("Welcome to the game")

    while try_remaining >0:
        print("\nWord to guess:",convert_pendu(word, found_letters))
        print("Try remaning: ", try_remaining)

        letter = input("propose a letter: ").lower()
    
        if letter in found_letters:
            print("you already  propose this letter!")
            continue

        found_letters.add(letter)
        if letter in word:
            print("good letter !")
            if all (letter in found_letters for letter in word):
                print("congracts you find the word  ", word)
                break

        else:
            print("wrong letter")
            try_remaining-=1

    if try_remaining == 0:
        print("you lose! the word was:",word)
hangman()