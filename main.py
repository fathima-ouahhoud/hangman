import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 750))
running = True

image = pygame.image.load('pendu_1.png').convert()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()