import pygame
from isp import drawing, load_image, load_score
from health import hearts

car_sprite = pygame.sprite.Group()
win = pygame.display.set_mode((720, 1000))
recscore = load_score('score.txt')
pygame.display.set_caption("Street Race")
road = load_image('road.png')
road1 = load_image('road.png')
score1 = 0

y = 0
x = 325
y1 = -1280
speed = 500
score1 = 0
health = 3
clock = pygame.time.Clock()
heart = load_image('heart.png', -1)
explosion = load_image('explosion2.png', -1)


def drawroad(tick):
    global y, y1
    y += speed * tick / 1000
    y1 += speed * tick / 1000
    if y > 1000:
        y -= 2280
    if y1 > 1000:
        y1 -= 2280
    drawing(win, road, 0, y)
    drawing(win, road1, 0, y1)


def writescore(score1):
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 24)
    score = myfont.render(str(round(score1)), True, (200, 255, 200))
    recordscore = myfont2.render("Record: " + str(recscore), True, (200, 255, 200))
    place = score.get_rect(center=(360, 50))
    place2 = score.get_rect(center=(560, 50))
    win.blit(score, place)
    win.blit(recordscore, place2)


def healthman(tick, healthp, heartgroup):
    if healthp == 3:
        hearts(heart, 50, 50, 250, tick, heartgroup)
        hearts(heart, 110, 50, 250, tick, heartgroup)
        hearts(heart, 170, 50, 250, tick, heartgroup)
    elif healthp == 2:
        hearts(heart, 50, 50, 350, tick, heartgroup)
        hearts(heart, 110, 50, 350, tick, heartgroup)
    elif healthp == 1:
        hearts(heart, 50, 50, 600, tick, heartgroup)
    else:
        pass