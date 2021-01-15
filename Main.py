import pygame
from isp import load_image, drawing, load_score, record
from Objects import spawning
import math
from visualinfo import drawroad, writescore, healthman

pygame.init()
pygame.font.init()
car_sprite = pygame.sprite.Group()
objects = pygame.sprite.Group()
hearts = pygame.sprite.Group()
road_group = pygame.sprite.Group()
win = pygame.display.set_mode((720, 1000))
recscore = load_score('score.txt')
pygame.display.set_caption("Street Race")
road = load_image('road.png')
road1 = load_image('road.png')
car_image = load_image('car.png', -1)
car_limage = load_image('carleft.png')
car_rimage = load_image('caright.png')
car_image = pygame.transform.scale(car_image, (90, 200))
car_limage = pygame.transform.scale(car_limage, (150, 175))
car_rimage = pygame.transform.scale(car_rimage, (150, 175))
car = pygame.sprite.Sprite()
car.image = car_image
car.rect = car_image.get_rect()
carmask = pygame.mask.from_surface(load_image('car.png'))
score1 = 0
objectmanager = 0
drawingcontrol = 0
spis = []

object1 = load_image('object1.png', -1)
object2 = load_image('object2.png', -1)
object3 = load_image('object3.png', -1)
object4 = load_image('object4.png', -1)
object5 = load_image('object5.png', -1)
object6 = load_image('object6.png', -1)
object7 = load_image('object7.png', -1)
object8 = load_image('object8.png', -1)
heart = load_image('heart.png', -1)

explosion = load_image('explosion2.png', -1)

objectss = [object1, object2, object3, object4, object5, object6, object7, object8]
for j in objectss[1:]:
    j = pygame.transform.scale(j, (70, 70))

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
ticksrecorder = 0
explosiontimer = 0
health = 3
healthcounter = 3

running = True
running2 = False
looose = False
looose1 = False


def damagevent():
    global health, looose, running, running2
    if pygame.sprite.collide_mask(car, objectmanager):
        health -= 1
        if health == 0:
            looose = True
            drawing(win, explosion, car.rect.x + car.rect.width // 2 - explosion.get_width() // 2,
                    car.rect.y - explosion.get_height() // 2)
            running = False
            running2 = True
        else:
            objectmanager.kill()
            objectmanager.rect.x += 1000


tick = clock.tick(60)
healthmanager = healthman(tick, health, hearts)

while running:
    tick = clock.tick(60)
    if not looose:
        win.fill((255, 255, 255))
        drawroad(tick)
        keys = pygame.key.get_pressed()
        score1 += speed * tick / (1000000 / 2)
        if score1 >= 1:
            speed = speedcontrol + round(math.log(int(score1), 2)) * 30
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if keys[pygame.K_RIGHT]:
                if not movingleft and not movingright:
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
        objects.draw(win)
        objects.update()
        if round(score1) // 3 != drawingcontrol and round(score1) != 0:
            drawingcontrol = round(score1) // 3
            objectmanager = spawning(objectss, speed, tick, spis, objects)
        car.rect.x = int(x)
        car.rect.y = 750
        car_sprite.draw(win)
        if int(recscore) < score1:
            recscore = int(round(score1))
            record(int(round(score1)))
        for j in objects:
            if j.rect.y > 1300:
                objects.remove(j)
        if healthcounter > health:
            hearts.empty()
            healthmanager = healthman(tick, health, hearts)
            healthcounter -= 1
        hearts.draw(win)
        hearts.update()
        writescore(score1)
        if score1 >= 3:
            damagevent()
    pygame.display.flip()

while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 35)
    score = myfont.render('You Lost!', True, (0, 0, 139))
    recordscore = myfont2.render("Your score is " + str(round(score1)), True, (0, 0, 139))
    place = (360 - score.get_width() // 2, 200)
    place2 = (360 - recordscore.get_width() // 2, 300)
    win.blit(score, place)
    win.blit(recordscore, place2)
    pygame.display.flip()

pygame.quit()