import pygame, sys

pygame.init()
screen = pygame.display.set_mode([600, 600])
font = pygame.font.Font(None, 30)
user_text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text [0:-1]
            else:
                user_text += event.unicode

    screen.fill((255, 255, 255))
    text_surface = font.render(user_text, True, (0, 0, 0))

    screen.blit(text_surface,(0, 0))
    pygame.display.flip()


#add words
#with open("words.txt", "a") as add_words:
#    file.write(f"\n{}")
#    word_added = font.render(f"Le mot {} à été ajouté")


 
#                if event.type == pygame.K_KP_ENTER:
#                   with open("words.txt", "a") as add_words:
#                    file.write(f"\n{user_text}")
#                    word_added = font.render(f"Le mot {user_text} à été ajouté")
