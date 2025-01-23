import pygame
pygame.init()
pygame.display.set_caption("Jeu du pendu")

screen = pygame.display.set_mode((800, 500))
black = [0, 0, 0]
white = [255, 255, 255]
blue = pygame.Color("azure3")

image = pygame.image.load('C:/Users/linda/OneDrive/Bureau/pendu/images/pendu_1.png').convert()
sans_font = pygame.font.SysFont("comicsansms", 28)
order = sans_font.render("Choissisez les bonnes lettres pour compléter le mot", False, black)
base_font = pygame.font.SysFont("comicsansms", 20)

user_letter =  ''
box = pygame.Rect(200, 200, 150, 30)


running = True

while running:

    for event in pygame.event.get():
        screen.fill(white)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_letter = user_letter[0:-1]
            else:
                user_letter += event.unicode 

    text_surface = base_font.render(user_letter, False,(0, 0, 0))
    
    screen.blit(order, (70, 20))
    screen.blit(image, (460, 79))

    pygame.draw.rect(screen, blue, box)
    screen.blit(text_surface,(box.x + 6, box.y + 1))
    box.w = max(150, text_surface.get_width() + 10)

    pygame.display.flip()

pygame.quit()

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