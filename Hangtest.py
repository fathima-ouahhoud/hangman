import pygame
import sys
import os 
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("comicsansms", 20)
sans_font = pygame.font.SysFont("comicsansms", 28)

# Colors
grey = (200, 220, 220)
black = (0, 0, 0)

# Game variables
difficulty = "medium"
current_page = "main"
score = 0
found_letters = set()
try_remaining = 6
word = ""


# Option buttons
option_rect = pygame.Rect(300,250,150,100)
play_rect = pygame.Rect(300,125,150,100)
quit_rect = pygame.Rect(300,380,150,100)
return_rect = pygame.Rect(300,470,150,100)
add_word_rect = pygame.Rect(300,300,200,100)
difficultie_rect = pygame.Rect(300,150,200,100)
easy_rect = pygame.Rect(100, 200, 150, 50)
medium_rect = pygame.Rect(300, 200, 150, 50)
hard_rect = pygame.Rect(500, 200, 150, 50)

# Images
images = [pygame.image.load(f'pendu_{i}.png').convert() for i in range(1, 8)]

# Word list
with open("words.txt", "r") as file:
    word_list = [word.strip() for word in file.readlines()]

def words_random():
    return random.choice(word_list)

def convert_hangman(word, found_letters):
    return " ".join([letter if letter in found_letters else "_" for letter in word])
 
#fonction principal
def draw_main_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, option_rect, 5)
    pygame.draw.rect(screen, black, play_rect, 5)
    pygame.draw.rect(screen, black, quit_rect, 5)
    screen.blit(font.render("PLAY", True, black), (play_rect.x + 20, play_rect.y + 40))
    screen.blit(font.render("OPTION", True, black), (option_rect.x + 20, option_rect.y + 30))
    screen.blit(font.render("QUIT", True, black), (quit_rect.x + 10, quit_rect.y + 30))

#fonction second
def draw_option_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, return_rect, 5)
    pygame.draw.rect(screen, black, difficulty_rect, 5)
    screen.blit(font.render("RETURN", True, black), (return_rect.x + 20, return_rect.y + 30))
    screen.blit(font.render("DIFFICULTY", True, black), (difficulty_rect.x + 10, difficulty_rect.y + 30))

def draw_difficulty_page():
    screen.fill(grey)
    pygame.draw.rect(screen, black, easy_rect, 5)
    pygame.draw.rect(screen, black, medium_rect, 5)
    pygame.draw.rect(screen, black, hard_rect, 5)
    screen.blit(font.render("EASY", True, black), (easy_rect.x + 30, easy_rect.y + 10))
    screen.blit(font.render("MEDIUM", True, black), (medium_rect.x + 10, medium_rect.y + 10))
    screen.blit(font.render("HARD", True, black), (hard_rect.x + 30, hard_rect.y + 10))
    
def draw_hangman_page(word_hangman, try_remaining):
    screen.fill(grey)
    hangman_text = font.render(word_hangman, True, black)
    screen.blit(hangman_text,(170,120))
    try_text = font.render(f"Try remaining: {try_remaining}",True, black)
    screen.blit(try_text,(150,70))

def handle_game_over(hangman_word):
    global current_page, score
    if "_" not in hangman_word:
        screen.blit(sans_font.render("You Win", False, black), (70, 20))
        score += 30
    else:
        screen.blit(sans_font.render("You Lose", False, black), (70, 20))
        score -= 20
    pygame.display.flip()
    pygame.time.delay(3000)
    current_page = "main"

# Main loop
main_page = True
in_game = False
found_letters = set()
mot = ""
try_remaining = 6
victory = False
easy_rect, medium_rect, hard_rect = None, None, None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_page == "main":
                if option_rect.collidepoint(event.pos):
                    current_page = "options"
                elif play_rect.collidepoint(event.pos):
                    current_page = "game"
                    word = words_random()
                    found_letters = set()
                    try_remaining = 6
                    score = 0
                    if difficulty == "easy":
                        try_remaining = 8
                    elif difficulty == "hard":
                        try_remaining = 4
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            elif current_page == "options":
                if return_rect.collidepoint(event.pos):
                    current_page = "main"
                elif difficulty_rect.collidepoint(event.pos):
                    current_page = "difficulty"

            elif current_page == "difficulty":
                if easy_rect.collidepoint(event.pos):
                    difficulty = "easy"
                    current_page = "options"
                elif medium_rect.collidepoint(event.pos):
                    difficulty = "medium"
                    current_page = "options"
                elif hard_rect.collidepoint(event.pos):
                    difficulty = "hard"
                    current_page = "options"

        if event.type == pygame.KEYDOWN:
            if current_page == "game":
                letter = event.unicode.lower()
                if letter in found_letters:
                    continue
                found_letters.add(letter)
                if letter not in word:
                    try_remaining -= 1

    if current_page == "main":
        draw_main_page()
    elif current_page == "game":
        hangman_word = convert_hangman(word, found_letters)
        draw_hangman_page(hangman_word, try_remaining)
        screen.blit(images[6 - try_remaining], (500, 120))  
        screen.blit(font.render(f"Score: {score}", True, black), (40, 400))

        if try_remaining == 0 or "_" not in hangman_word:
            handle_game_over(hangman_word)

    elif current_page == "options":
        draw_option_page()
    elif current_page == "difficulty":
        draw_difficulty_page()

    pygame.display.flip()
