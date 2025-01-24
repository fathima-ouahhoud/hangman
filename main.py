import pygame
import sys
import os 
import random


pygame.init()


screen = pygame.display.set_mode((800, 600))
font_path = os.path.join(r'C:\Users\nadjl\PressStart2P-Regular.ttf')
size = 19
# Colors
grey = (200, 220, 220)
black = (0, 0, 0)


pygame.display.set_caption("Pendu")


font = pygame.font.SysFont("comicsansms", 20)

# Option buttons
option_rect = pygame.Rect(300,250,150,100)
play_rect = pygame.Rect(300,125,150,100)
quit_rect = pygame.Rect(300,380,150,100)
return_rect = pygame.Rect(300,470,150,100)
add_word_rect = pygame.Rect(300,300,200,100)
difficultie_rect = pygame.Rect(300,150,200,100)


#word list 
words = open("words.txt", "r")

f = words.readlines()
list_word = []
for line in f:
    if (line[-1] == '\n'):
        list_word.append(line[:-1])
    else:
        list_word.append(line)
print(list_word)



with open("words.txt","w") as file:
    for word in words:
        file.write(word +"\n")

def words_random(file):
    with open (file,"r") as f:
        words = f.read().splitlines()
    return random.choice(words)
    
def convert_hangman(word, found_letters):
    return " ".join([letter if letter in found_letters else "_" for letter in word])
 



#fonction principal
def draw_main_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, option_rect, 5)
    pygame.draw.rect(screen, black, play_rect, 5)
    pygame.draw.rect(screen, black, quit_rect, 5)
    play_text = font.render("PLAY", True, black)
    option_text = font.render("OPTION", True, black)
    quit_text = font.render("QUIT",True, black)
    screen.blit(option_text, (option_rect.x + 20, option_rect.y + 30))
    screen.blit(play_text, (play_rect.x+ 20, play_rect.y + 40))
    screen.blit(quit_text, (quit_rect.x + 10, quit_rect.y + 30))

#fonction second
def draw_option_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, add_word_rect, 5)
    pygame.draw.rect(screen, black, difficultie_rect, 5)
    pygame.draw.rect(screen, black, return_rect, 5)
    add_word_text = font.render("ADD WORDS", True, black)
    dificultie_text = font.render("DIFFICULTY", True, black)
    return_text = font.render("RETURN", True, black)
    screen.blit(add_word_text, (add_word_rect.x + 10, add_word_rect.y+ 30))
    screen.blit(dificultie_text, (difficultie_rect.x + 10, difficultie_rect.y + 30))
    screen.blit(return_text, (return_rect.x + 20, return_rect.y + 30,))

def draw_hangman_page(word_hangman, try_remaining):
    screen.fill(grey)
    hangman_text = font.render(word_hangman, True, black)
    screen.blit(hangman_text,(110,130))
    try_text = sans_font.render(f"Try remaining : {try_remaining}",True, black)
    screen.blit(try_text,(100,70))


# victory/lose render
sans_font = pygame.font.SysFont("comicsansms", 28)
image = pygame.image.load('images/pendu_1.png').convert()
win_condition = sans_font.render("You Win", True, black)
lose_condition = sans_font.render(f"You Lose, the word was :", True, black)
false_letters = sans_font.render("Wrong letters", True, black)




# Main loop
main_page = True
in_game = False
found_letters = set()
mot = ""
try_remaining = 6
victory = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_page:
                if option_rect.collidepoint(event.pos):
                    main_page = False
                elif play_rect.collidepoint(event.pos):
                    main_page = False
                    in_game = True
                    word = words_random("words.txt")
                    found_letters = set()
                    try_remaining = 6
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            else:
                if return_rect.collidepoint(event.pos):
                    main_page = True
                    in_game = False

            if main_page and option_rect.collidepoint(event.pos):
                main_page = False
            if main_page and play_rect.collidepoint(event.pos):
                main_page = False
            else:
                if return_rect.collidepoint(event.pos):
                    main_page = True
        if in_game and event.type == pygame.KEYDOWN:
            letter = event.unicode.lower()
            if letter in found_letters:
                continue
            found_letters.add(letter)
            if letter not in word:
                try_remaining -=1
            

    if main_page:
        draw_main_page()
    elif in_game:
        hangman_word = convert_hangman(word, found_letters)
        draw_hangman_page(hangman_word, try_remaining)
        screen.blit(image, (480, 120))
        screen.blit(false_letters, (100, 220))



        if "_" not in hangman_word.replace("",""):
            screen.blit(win_condition, (100, 20))
        
        if try_remaining == 5:
            image = pygame.image.load('images/pendu_2.png').convert()
        elif try_remaining == 4:
            image = pygame.image.load('images/pendu_3.png').convert()
        elif try_remaining == 3:
            image = pygame.image.load('images/pendu_4.png').convert()
        elif try_remaining == 2:
            image = pygame.image.load('images/pendu_5.png').convert()
        elif try_remaining == 1:
            image = pygame.image.load('images/pendu_6.png').convert()
        elif try_remaining == 0:
            image = pygame.image.load('images/pendu_7.png').convert()
            screen.blit(lose_condition, (100, 400))




    else:
        draw_option_page()
    
    pygame.display.flip()


# afficher une liste de mots
#fichier = open("mots.txt", "r")
#f = fichier.readlines()
#listsans = []
#for ligne in f:
#    if (ligne[-1] == '\n'):
#        listsans.append(ligne[:-1])
#    else:
#        listsans.append(ligne)
#print(listsans)

# rajouter des mots
#fichier = open("mots.txt", "w")
#fichier.write("objet\n")
#fichier.close()