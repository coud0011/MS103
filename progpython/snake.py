# -------------------------------------------------------------------------------
# Name:        jeu du snake
# Purpose:      jouer un serpent qui avance et mange puis grandis
#
# Author:      Coudrot Axel
#
# Created:     16/10/2022
# Copyright:   (c) axel 2022
# Licence:     <axel licence>
# -------------------------------------------------------------------------------

# Jeu du snake cree par axel, le 16/10/2022 en Python 3.7 avec le module OpenGL


# import des fonctions speciales
import code
from os import _exit
from tkinter import mainloop
from OpenGL.GL import *
from OpenGL.GLUT import *
from random import randint

# creation des variables
from OpenGL.raw.GLUT import glutSwapBuffers

window = 0  # nde fenetre GLUT
width, height = 900, 500  # taille de la fenetre
field_width, field_height = 90, 50  # resolution
interval = 100
food = []  # liste de typer (x, y)
snake = [(20, 20)]  # liste des positions (x,y) du serpent
snake_dir = (1, 0)  # direction du mouvement du serpent
i = 0

# definition des fonctions

def refresh2d_custom(widthrect, height, internal_width, internal_height):
    glViewport(0, 0, widthrect, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)  # dessine un rectangle
    glVertex2f(x, y)  # coin bas gauche
    glVertex2f(x + width, y)  # coin bas droit
    glVertex2f(x + width, y + height)  # coin haut droit
    glVertex2f(x, y + height)  # coin haut gauche
    glEnd()  # fin du rectangle


def draw():  # definition de la fonction draw
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # efface l'ecran
    glLoadIdentity()  # remise a 0 de la position
    refresh2d_custom(width, height, field_width, field_height)  # ICI : dessiner des motifs
    draw_food()  # dessine la nourriture
    draw_snake()  # dessine le serpent
    glutSwapBuffers()  # double tampon
    dead()


def draw_snake():
    #print(snake)
    glColor3f(1.0, 1.0, 1.0)  # definition de la couleur en blanc
    head = snake[0]
    count = 0
    for (x, y) in snake:  # passe par chaque entree (x, y)
        if count != 0 and count != len(snake) - 1 and (x, y) == head:
            print("game over : you touched yourself")
            glutLeaveMainLoop()
        draw_rect(x, y, 1, 1)  # dessine en (X, y) un rectangle avec largeur = 1 et hauteur =1
        count += 1


def vec_add(toc, tic):
    (x1, y1) = toc
    (x2, y2) = tic
    return (x1 + x2, y1 + y2)


def update(value):  # ICI mise a jour des elements glutTimerFunc(interval, update, 0)
    # deplacement du serpent
    snake.insert(0, vec_add(snake[0], snake_dir))  # insere une nouvelle position au debut de la liste
    snake.pop()  # supprime la derniere valeur de la liste
    # spawn de la nourriture
    r = randint(0, 20)  # regenere de la nourriture avec une chance de 5%
    if r == 0:
        x, y = randint(0, field_width), randint(0, field_height)
        food.append((x, y))
    glutTimerFunc(interval, update, 0)  # declenche la mise a jour


def keyboard(*args):
    global snake_dir
    print(args[0])
    if args[0] == 101:
        snake_dir = (0, 1)
        print('haut')  # vers le haut
    if args[0] == 103:
        snake_dir = (0, -1)  # vers le bas
        print('bas')
    if args[0] == 100:
        snake_dir = (-1, 0)  # vers la gauche
        print('gauche')
    if args[0] == 102:
        snake_dir = (1, 0)  # vers la droite
        print('droite')


def draw_food():
    glColor3f(0.5, 0.5, 1.0)  # selectionne la couleur bleue

    for x, y in food:  # passe en revue les coordonnees x et y de la liste
        draw_rect(x, y, 1, 1)  # dessine la nourriture a la position (x, y) avec largeur 1 et hauteur 1

    #   le serpent mange la nourriture
    (hx, hy) = snake[0]  # memorise la position x et y de la tete du serpent
    for x, y in food:  # passe en revue la liste de la nourriture
        if hx == x and hy == y:  # est-ce que la position de la tete du serpent correspond a celle de la nourriture?
            snake.append((x, y))  # allonge le serpent
            food.remove((x, y))  # efface la nourriture de l'ecran
def dead():
    (hx, hy) = snake[0]
    if hx==0 or hy==0 or hx==90 or hy==50:  #gauche haut droit bas
        print("game over")
        glutLeaveMainLoop()

# programme en lui meme
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)  # taille de la fenetre
glutInitWindowPosition(0, 0)  # position de la fenetre
glutCreateWindow("Jeu du Snake @Lords_axs")  # cree la fenetre avec titre
glutDisplayFunc(draw)  # fonction draw
glutIdleFunc(draw)  # Poursuit le dessin
glutTimerFunc(interval, update, 0)  # mise a jour
glutKeyboardFunc(keyboard)  # indique a open gl que nous verifions les clavier
glutSpecialFunc(keyboard)
glutMainLoop()  # demarre la routine
