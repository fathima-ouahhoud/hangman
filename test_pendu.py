import random

mots = ["trottinette", "plante", "gourde", "projecteur", "elephan", "casque", "voile"]

with open("mots.txt","w") as fichier:
    for mot in mots:
        fichier.write(mot + "\n")

#print("Menu")
#print("Jouer une partie == 1 ")
#print("Insérer un nouveau mot == 2")

#choisir un mots aléatoirement
def mot_aleatoire(fichier):
    with open (fichier, 'r') as f:
        mots = f.read().splitlines()
    return(random.choice(mots))
 
#pour mettre les underscore a la place des lettres
def convertir_pendu(mot, lettres_trouvees):
    return ' '.join([lettre if lettre in lettres_trouvees else "_" for lettre in mot])
#debut d'un pendu
def pendu():
    mot = mot_aleatoire("mots.txt")
    lettres_trouvees = set()
    essaie_restant = 6
    print("bienvenue dans le jeu")

    while essaie_restant >0:
        print("\nMots à deviner:",convertir_pendu(mot, lettres_trouvees))
        print("Essaie restant: ", essaie_restant)

        lettre = input("proposer une lettre: ").lower()
    
        if lettre in lettres_trouvees:
            print("vous avez deja proposer cette lettre!")
            continue

        lettres_trouvees.add(lettre)
        if lettre in mot:
            print("bonne lettre !")
            if all (lettre in lettres_trouvees for lettre in mot):
                print("felicitation vous avez devenie le mot ", mot)
                break

        else:
            print("mauvaise lettre")
            essaie_restant-=1

    if essaie_restant == 0:
        print("vous avez perdu! le mot etait :",mot)
pendu()