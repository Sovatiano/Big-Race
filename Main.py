import pygame
from isp import load_image, drawing, load_score, record
import math


pygame.init()
pygame.font.init()
car_sprite = pygame.sprite.Group()
win = pygame.display.set_mode((720, 1000))
recscore = load_score('score.txt')
pygame.display.set_caption("Street Race")
road = load_image('road.png')
road1 = load_image('road.png')
car_image = load_image('car.png')
car_limage = load_image('carleft.png')
car_rimage = load_image('caright.png')
car_image = pygame.transform.scale(car_image, (75, 150))
car_limage = pygame.transform.scale(car_limage, (131, 160))
car_rimage = pygame.transform.scale(car_rimage, (131, 160))
car = pygame.sprite.Sprite()
car.image = car_image
car.rect = car_image.get_rect()
score1 = 0

car_sprite.add(car)

clock = pygame.time.Clock()
y = 0
x = 325
y1 = -1280
speed = 500
speedcontrol = 500
carspeed = 20000
car.rect.x = 325
score1 = 0
movingright = False
movingleft = False


running = True

while running:
    tick = clock.tick()
    win.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    score1 += speed * tick / (1000000 / 2)
    if score1 >= 1:
        speed = speedcontrol + math.log(int(score1), 2) // 1 * 130
    print(speed, score1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_RIGHT]:
            if not movingleft and not  movingright:
                if x != 565:
                    x += carspeed / 1000
                movingleft = False
                movingright = True
                coords = car.rect.x
        if keys[pygame.K_LEFT]:
            if not movingleft and not movingright:
                if x != 85:
                    x -= carspeed / 1000
                movingright = False
                movingleft = True
                coords = car.rect.x
    if movingright:
        if x < 565:
            if x != 565 and x != 325 and x != 85:
                car.image = car_rimage
                x += carspeed / 1000
            else:
                car.image = car_image
                movingright = False
        else:
            car.image = car_image
            movingright = False
    if movingleft:
        if x > 85:
            if x != 565 and x != 325 and x != 85:
                car.image = car_limage
                x -= carspeed / 1000
            else:
                car.image = car_image
                movingleft = False
        else:
            car.image = car_image
            movingleft = False
    drawing(win, road, 0, y)
    drawing(win, road1, 0, y1)
    car.rect.x = int(x)
    car.rect.y = 750
    car_sprite.draw(win)
    y += speed * tick / 1000
    y1 += speed * tick / 1000
    if int(recscore) < score1:
        recscore = int(round(score1))
        record(int(round(score1)))
    if y > 1000:
        y -= 2280
    if y1 > 1000:
        y1 -= 2280
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 24)
    score = myfont.render(str(round(score1)), True, (200, 255, 200))
    recordscore = myfont2.render("Record: " + str(recscore), True, (200, 255, 200))
    place = score.get_rect(center=(360, 50))
    place2 = score.get_rect(center=(560, 50))
    win.blit(score, place)
    win.blit(recordscore, place2)
    pygame.display.flip()
pygame.quit()