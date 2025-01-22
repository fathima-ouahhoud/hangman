import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Jeu du pendu")
running = True
white = [255, 255, 255]


image = pygame.image.load('C:/Users/linda/OneDrive/Bureau/pendu/images/pendu_1.png').convert()

while running:
    for event in pygame.event.get():
        screen.fill(white)
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, (450, 79))
    pygame.display.flip()

pygame.quit()