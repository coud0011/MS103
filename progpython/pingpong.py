#programme non fonctionnel





# pyg0110_ping_pong.py

import pygame
from pygame.locals import *
import os
import pynput

# Pour positionner la fenêtre Pygame.
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (120, 200)

# Initialisation des modules de Pygame
pygame.init()

# Permet de rendre la fenêtre de taille ajustable.
fenetre = pygame.display.set_mode((640,480), RESIZABLE)

# Une image pour le fond de la fenêtre
fond = pygame.image.load("images/background_herbe.jpg").convert()
perso1 = pygame.image.load("images/perso_1.png").convert_alpha()
joueur1= pygame.image.load("images/mario.png").convert_alpha()
joueur2= pygame.image.load("images/luigi.png").convert_alpha()

# Redimensionne la taille de l'image

perso1 = pygame.transform.scale(perso1, (40,40))
joueur1 = pygame.transform.scale(joueur1, (50,50))
joueur2 = pygame.transform.scale(joueur2, (50,50))

# Affiche l'image dans la fenêtre
fenetre.blit(fond, (0, 0))

# Affiche le personnage au-dessus de l'herbe
fenetre.blit(perso1, (200, 200))
fenetre.blit(joueur1, (200, 200))
fenetre.blit(joueur2, (200, 200)) 

# Actualise la fenêtre
pygame.display.flip()

PosX = 200 # Position en X du perso1
PosY = 210 # Position en Y du perso1
marX = 50 # Position en X du joueur1
marY = 210 # Position en Y du joueur1
luiX = 550 # Position en X du joueur2
luiY = 210 # Position en Y du joueur2
DirX = 2   # Direction X de déplacement de perso1
DirY = 1.89   # Direction Y de déplacement de perso1

# Pour avoir un autorepeat si une touche est pressée.
pygame.key.set_repeat(10, 3) # répétition de la touche toutes les ... [ms]

# Pour définir une vitesse d'exécution,
# en limitant en attendant qu'un certain temps se soit écoulé avant de continuer.
myClock = pygame.time.Clock()

# Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1
x=0
def show(key):
    if key==Key.z:
        marY+=10
    if key==Key.s:
        marY-=10
    if key==Key.arrow_upper:
        luiY+=10
    if key==Key.arrow_lower:
        luiY-=10
# ================================================
# Boucle principale
while continuer:

    # Boucle sur tous les événements gérés par Pygame
    for event in pygame.event.get():        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # La fenêtre a été fermée ou La touche ESC a été pressée.
            continuer = 0 # Indique de sortir de la boucle.
    from pynput.keyboard import Key, Listener
    with Listener(on_press = show) as listener:
        listener.join()
    # Affiche le fond
    fenetre.blit(fond, (0, 0))

    # Affiche l'image de perso1
    fenetre.blit(perso1, (PosX, PosY))
    fenetre.blit(joueur1, (marX, marY))
    fenetre.blit(joueur2, (luiX, luiY))
    # Mouvement automatique de perso1
    if x==10:
        PosX = PosX + DirX
        PosY = PosY + DirY
        x=0

    if (luiX+15 > PosX > luiX-15 and luiY+15 > PosY > luiY-15):
        DirX = -DirX
        # Accélère le mouvement de perso1
        DirX -= 0.2

    if (marX+15 > PosX > marX-15 and marY+15 > PosY > marY-15):
        # Rebondi sur la paroi de gauche
        DirX = -DirX
        # Accélère le mouvement de perso1
        DirX += 0.2
    
    if (PosY < 1):
        # Rebondi sur la paroi du haut
        DirY = -DirY
            
    if (PosY > 450):
        # Rebondi sur la paroi du bas
        DirY = -DirY
    
    x+=1
    # Actualise la fenêtre
    pygame.display.flip()
    if (PosX > 600):
        pygame.display.quit() # ferme la fenêtre 
        print("Mario Wins!")
    if (PosX < 0):
        pygame.display.quit() # ferme la fenêtre
        print("Luigi Wins!")

    # Limitation de la vitesse à ... images par seconde
    # 120 => attend que 1000 / 120 [ms] se soit écoulé depuis le dernier appel,
    # avant de continuer.
    # 120 => limite à 120 images par secondes, soit 20 exécutions de la boucle par seconde
    myClock.tick(300) 

pygame.display.quit() # ferme la fenêtre
pygame.quit() # quitte pygame