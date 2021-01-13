import pygame
import os
import sys
import math

carspeed = 10


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def load_score(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с текстом '{fullname}' не найден")
        sys.exit()
    f = open(fullname)
    score = f.read()
    return score

def record(score):
    fullname = os.path.join('data', 'score.txt')
    if not os.path.isfile(fullname):
        print(f"Файл с текстом '{fullname}' не найден")
        sys.exit()
    f = open(fullname, 'w')
    f.write(str(round(score)))


def drawing(screen_name, image, x, y):
    screen_name.blit(image, (x, y))

