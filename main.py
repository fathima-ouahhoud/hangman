import pygame
import sys
import os 
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Colors
grey = (200, 220, 220)
black = (0, 0, 0)

pygame.display.set_caption("Hangman")
font = pygame.font.SysFont(None, 30)


# Option buttons
option_rect = pygame.Rect(300,250,150,100)
play_rect = pygame.Rect(300,125,150,100)
quit_rect = pygame.Rect(300,380,150,100)
return_rect = pygame.Rect(50,470,150,100)
add_word_rect = pygame.Rect(300,300,200,100)


with open("words.txt", "r") as file:
    word_list = [word.strip() for word in file.readlines()]

def words_random(file):
    with open (file,"r") as f:
        words = f.read().splitlines()
    return (random.choice(words))
    
def convert_hangman(word, found_letters):
    return " ".join([letter if letter in found_letters else "_" for letter in word])

 
#fonction principal
def draw_main_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, option_rect, 5)
    pygame.draw.rect(screen, black, play_rect, 5)
    pygame.draw.rect(screen, black, quit_rect, 5)
    play_text = font.render("PLAY", True, black)
    words_text = font.render("ADD WORDS", True, black)
    quit_text = font.render("QUIT",True, black)
    screen.blit(words_text, (option_rect.x + 20, option_rect.y + 30))
    screen.blit(play_text, (play_rect.x+ 20, play_rect.y + 40))
    screen.blit(quit_text, (quit_rect.x + 10, quit_rect.y + 30))


#fonction second
def words_option_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, return_rect, 5,)
    return_text = font.render("RETURN", True, black)
    screen.blit(return_text, (return_rect.x + 20, return_rect.y + 30,))

#add words
add_words = open("words.txt", "a")




def draw_hangman_page(word_hangman, try_remaining):
    screen.fill(grey)
    hangman_text = font.render(word_hangman, True, black)
    screen.blit(hangman_text,(170,120))
    try_text = font.render(f"Try remaining: {try_remaining}",True, black)
    screen.blit(try_text,(150,70))



image = pygame.image.load('images\pendu_1.png').convert()
win_condition = font.render("You Win", False, black)
lose_condition = font.render("You Lose", False, black)


score = 0
# Main loop
main_page = True
in_game = False
found_letters = set()
mot = ""
try_remaining = 6
victory = False
add_words = False


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
                    score = 0
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            else:
                if return_rect.collidepoint(event.pos):
                    main_page = True
                    in_game = False


        if in_game and event.type == pygame.KEYDOWN:
            letter = event.unicode.lower()
            if letter in found_letters:
                continue
            found_letters.add(letter)
            if letter not in word:
                try_remaining -=1
            else:
                score += 10 


    if main_page:
        draw_main_page()
    elif in_game:
        hangman_word = convert_hangman(word, found_letters)
        draw_hangman_page(hangman_word, try_remaining)
        screen.blit(image, (470, 120))

        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text,(40, 400))


        if "_" not in hangman_word.replace("",""):
            screen.blit(win_condition, (70, 20))
            score += 30
            pygame.display.flip()
            pygame.time.delay(3000)
            main_page = True
            in_game = False


        elif try_remaining == 0:
            screen.blit(lose_condition, (150, 20))
            image = pygame.image.load('images\pendu_7.png').convert()
            score -= 20
            pygame.display.flip()
            pygame.time.delay(3000)
            main_page = True
            in_game = False


        elif try_remaining == 1:
            image = pygame.image.load('images\pendu_6.png').convert()
        elif try_remaining == 2:
            image = pygame.image.load('images\pendu_5.png').convert()
        elif try_remaining == 3:
            image = pygame.image.load('images\pendu_4.png').convert()
        elif try_remaining == 4:
            image = pygame.image.load('images\pendu_3.png').convert()
        elif try_remaining == 5:
            image = pygame.image.load('images\pendu_2.png').convert()


    else:
        words_option_page()
    
    pygame.display.flip()