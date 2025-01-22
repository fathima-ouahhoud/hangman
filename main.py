import pygame
pygame.init()
pygame.display.set_caption("Jeu du pendu")
file = open("mots.txt", "r")
read = file.readline()

running = True
screen = pygame.display.set_mode((800, 500))
white = [255, 255, 255]
black = [0, 0, 0]
image = pygame.image.load('C:/Users/linda/OneDrive/Bureau/pendu/images/pendu_1.png').convert()
arial_font = pygame.font.SysFont("Arial", 25)
order = arial_font.render("Choissisez les bonnes lettres pour compléter le mot", True, black)

#plesk > httpdocs > index 
#repository pour actualiser à partir de git

while running:

    for event in pygame.event.get():
        screen.fill(white)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(order, (30, 20))
    screen.blit(read, (20, 30))

    screen.blit(image, (460, 79))

    pygame.display.flip()

pygame.quit()