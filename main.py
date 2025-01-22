import pygame
pygame.init()
pygame.display.set_caption("Jeu du pendu")

screen = pygame.display.set_mode((800, 500))
black = [0, 0, 0]
white = [255, 255, 255]
image = pygame.image.load('C:/Users/linda/OneDrive/Bureau/pendu/images/pendu_1.png').convert()
arial_font = pygame.font.SysFont("Arial", 22)
order = arial_font.render("Choissisez les bonnes lettres pour compléter le mot", False, black)

running = True

while running:

    for event in pygame.event.get():
        screen.fill(white)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(order, (30, 20))

    screen.blit(image, (460, 79))

    pygame.display.flip()

pygame.quit()