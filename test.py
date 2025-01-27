import pygame, sys

pygame.init()
clock = pygame.time.Clock
screen = pygame.display.set_mode([600, 600])
font = pygame.font.Font(None, 30)
text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text [0:-1]
            else:
                text += event.unicode

    screen.fill((255, 255, 255))
    text_surface = font.render(text, True, (0, 0, 0))

    screen.blit(text_surface,(0, 0))
    pygame.display.flip()
