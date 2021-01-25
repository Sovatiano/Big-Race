import pygame
from isp import load_image, drawing, load_score, record
from Objects import spawning
import math, random
from visualinfo import drawroad, writescore, healthman, TireMarks, DopHearts, Shields

pygame.init()
pygame.font.init()
car_sprite = pygame.sprite.Group()
objects = pygame.sprite.Group()
hearts = pygame.sprite.Group()
dophearts = pygame.sprite.Group()
shileds = pygame.sprite.Group()
road_group = pygame.sprite.Group()
tiremarkss = pygame.sprite.Group()
win = pygame.display.set_mode((720, 1000))
recscore = load_score('score.txt')
pygame.display.set_caption("Street Race")
road = load_image('road.png')
road1 = load_image('road.png')
car_image = load_image('car.png', -1)
car_limage = load_image('carleft.png')
car_rimage = load_image('caright.png')
car_imageshield = load_image('carshield.png', -1)
car_limageshield = load_image('carleftshield.png')
car_rimageshield = load_image('carightshield.png')
car_image = pygame.transform.scale(car_image, (90, 200))
car_limage = pygame.transform.scale(car_limage, (150, 175))
car_rimage = pygame.transform.scale(car_rimage, (150, 175))
car_imageshield = pygame.transform.scale(car_imageshield, (90, 200))
car_limageshield = pygame.transform.scale(car_limageshield, (150, 175))
car_rimageshield = pygame.transform.scale(car_rimageshield, (150, 175))
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
shield = load_image('shield.png', -1)
shield = pygame.transform.scale(shield, (75, 92))

explosion = load_image('explosion2.png', -1)

restartbutton = load_image('PlayButton.png', -1)
quitbutton = load_image('QuitButton.png', -1)
tiremark = load_image('tiremark.png')
tiremarkl = load_image('tiremarkl.png')
tiremark = pygame.transform.scale(tiremark, (100, 100))
tiremarkl = pygame.transform.scale(tiremarkl, (100, 100))

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
n = 0
z = 1
movingright = False
movingleft = False
ticksrecorder = 0
explosiontimer = 0
health = 3
healthcounter = 3

running0 = True
running = True
running2 = False
looose = False
looose1 = False
onemoreframe = True
drawmarks = False
shieldisactive = False
shieldtimer = 0
shieldwidth = 0


def damagevent(moreframe):
    global health, looose, running, running2, healthcounter, speedcontrol, healthmanager, shieldisactive, shieldtimer, \
        shieldwidth
    if pygame.sprite.collide_mask(car, objectmanager):
        health -= 1
        shieldisactive = False
        shieldtimer = 0
        shieldwidth = 0
        if health <= 0:
            if not moreframe:
                looose = True
                if movingleft:
                    drawing(win, explosion, car.rect.x + car.rect.width // 2 - explosion.get_width() // 2 - 60,
                            car.rect.y - explosion.get_height() // 2)
                if movingright:
                    drawing(win, explosion, car.rect.x + car.rect.width // 2 - explosion.get_width() // 2 + 60,
                            car.rect.y - explosion.get_height() // 2)
                if not movingleft and not movingright:
                    drawing(win, explosion, car.rect.x + car.rect.width // 2 - explosion.get_width() // 2,
                            car.rect.y - explosion.get_height() // 2)
                running = False
                running2 = True
        else:
            objectmanager.kill()
            objectmanager.rect.x += 1000

    if pygame.sprite.collide_mask(car, dopherman):
        if not shieldisactive:
            if health <= 2:
                health += 1
                healthcounter += 1
                hearts.empty()
                if shieldisactive:
                    healthmanager = healthman(tick, health - 1, hearts)
                else:
                    healthmanager = healthman(tick, health, hearts)
                dopherman.kill()
                dopherman.rect.x += 1000
        else:
            if health <= 3:
                health += 1
                healthcounter += 1
                hearts.empty()
                if shieldisactive:
                    healthmanager = healthman(tick, health - 1, hearts)
                else:
                    healthmanager = healthman(tick, health, hearts)
                dopherman.kill()
                dopherman.rect.x += 1000

    if pygame.sprite.collide_mask(car, shiledman):
        if not shieldisactive:
            health += 1
            shieldisactive = True
            shiledman.kill()
            shiledman.rect.x += 1000
            if shieldtimer != 0:
                shieldtimer += 300 - shieldtimer
                shieldwidth += 300 - shieldwidth
            else:
                shieldtimer += 300
                shieldwidth += 300
        if shieldisactive:
            shiledman.kill()
            shiledman.rect.x += 1000
            if shieldtimer != 0:
                shieldtimer += 300 - shieldtimer
                shieldwidth += 300 - shieldwidth
            else:
                shieldtimer += 300
                shieldwidth += 300


def drawshield(width):
    global shield
    drawing(win, shield, 300 - shield.get_width() // 2, 100)
    pygame.draw.rect(win, "blue", (360, 100, width, 25))


tick = clock.tick(60)
if shieldisactive:
    healthmanager = healthman(tick, health - 1, hearts)
else:
    healthmanager = healthman(tick, health, hearts)
dopherman = DopHearts(speed, tick, heart, dophearts)
shiledman = Shields(speed, tick, shield, shileds)

while running0:
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
                    running0 = False
                if keys[pygame.K_RIGHT]:
                    if not movingleft and not movingright:
                        if x != 565:
                            TireMan = TireMarks(speed, tick, car.rect.x + 60, car.rect.y + 60, tiremark, tiremarkss)
                            x += carspeed / 1000
                        movingleft = False
                        movingright = True
                        coords = car.rect.x
                if keys[pygame.K_LEFT]:
                    if not movingleft and not movingright:
                        if x != 85:
                            TireMan = TireMarks(speed, tick, car.rect.x - 30, car.rect.y + 60, tiremarkl, tiremarkss)
                            x -= carspeed / 1000
                        movingright = False
                        movingleft = True
                        coords = car.rect.x
            if movingright:
                if x < 565:
                    if x != 565 and x != 325 and x != 85:
                        if shieldisactive:
                            car.image = car_rimageshield
                        else:
                            car.image = car_rimage
                        x += carspeed / 1000
                    else:
                        if shieldisactive:
                            car.image = car_imageshield
                        else:
                            car.image = car_image
                        movingright = False
                else:
                    if shieldisactive:
                        car.image = car_imageshield
                    else:
                        car.image = car_image
                    movingright = False
            if movingleft:
                if x > 85:
                    if x != 565 and x != 325 and x != 85:
                        if shieldisactive:
                            car.image = car_limageshield
                        else:
                            car.image = car_limage
                        x -= carspeed / 1000
                    else:
                        if shieldisactive:
                            car.image = car_imageshield
                        else:
                            car.image = car_image
                        movingleft = False
                else:
                    if shieldisactive:
                        car.image = car_imageshield
                    else:
                        car.image = car_image
                    movingleft = False
            if not movingleft and not movingright and not shieldisactive:
                car.image = car_image
            if not movingright and not movingleft and shieldisactive:
                car.image = car_imageshield
            objects.draw(win)
            objects.update()
            if not shieldisactive:
                if health == 2:
                    n = random.randint(1, 101)
                    z = random.randint(1, 101)
                if health == 1:
                    n = random.randint(1, 76)
                    z = random.randint(1, 76)
                if n == z and len(dophearts) == 0:
                    dopherman = DopHearts(speed, tick, heart, dophearts)
            else:
                if health == 3:
                    n = random.randint(1, 1001)
                    z = random.randint(1, 1001)
                if health == 2:
                    n = random.randint(1, 501)
                    z = random.randint(1, 501)
                if n == z and len(dophearts) == 0:
                    dopherman = DopHearts(speed, tick, heart, dophearts)
            q = random.randint(1, 1001)
            w = random.randint(1, 1001)
            if q == w and len(shileds) == 0:
                shiledman = Shields(speed, tick, shield, shileds)
            if round(score1) // 3 != drawingcontrol and round(score1) != 0:
                drawingcontrol = round(score1) // 3
                objectmanager = spawning(objectss, speed, tick, spis, objects)
            car.rect.x = int(x)
            car.rect.y = 750
            tiremarkss.draw(win)
            tiremarkss.update()
            dophearts.draw(win)
            dophearts.update()
            shileds.draw(win)
            shileds.update()
            car_sprite.draw(win)
            if int(recscore) < score1:
                recscore = int(round(score1))
                record(int(round(score1)))
            for j in objects:
                if j.rect.y > 1300:
                    objects.remove(j)
            for j in tiremarkss:
                if j.rect.y > 1300:
                    tiremarkss.remove(j)
            for j in dophearts:
                if j.rect.y > 2000 or score1 < 3:
                    dophearts.remove(j)
            for j in shileds:
                if j.rect.y > 2000 or score1 < 3:
                    shileds.remove(j)
            if healthcounter > health:
                hearts.empty()
                if shieldisactive:
                    healthmanager = healthman(tick, health - 1, hearts)
                else:
                    healthmanager = healthman(tick, health, hearts)
                healthcounter -= 1
                if health == 0:
                    onemoreframe = False
            hearts.draw(win)
            hearts.update()
            writescore(score1, recscore)
            if int(recscore) < score1:
                recscore = int(round(score1))
                record(int(round(score1)))
            if shieldisactive and shieldtimer > 0:
                shieldwidth -= 1
                drawshield(shieldwidth)
                shieldtimer -= 1
                if shieldtimer == 1:
                    health -= 1
                    shieldisactive = False
            if score1 >= 3:
                damagevent(onemoreframe)
        pygame.display.flip()

    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
                running0 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 360 - restartbutton.get_width() // 2 <= event.pos[
                    0] <= 360 + restartbutton.get_width() // 2 and 600 <= event.pos[
                    1] <= 600 + restartbutton.get_height():
                    if event.button == 1:
                        running0 = False
                        running2 = False
                if 360 - restartbutton.get_width() // 2 <= event.pos[
                    0] <= 360 + restartbutton.get_width() // 2 and 400 <= event.pos[
                    1] <= 400 + restartbutton.get_height():
                    if event.button == 1:
                        clock = pygame.time.Clock()
                        y = 0
                        x = 325
                        y1 = -1280
                        speed = 500
                        speedcontrol = 500
                        carspeed = 20000
                        car.rect.x = 325
                        movingright = False
                        movingleft = False
                        ticksrecorder = 0
                        explosiontimer = 0
                        health = 3
                        healthcounter = 3
                        running0 = True
                        running = True
                        running2 = False
                        looose = False
                        looose1 = False
                        onemoreframe = True
                        objects.empty()
                        car.image = car_image
                        score1 = 0
                        objectmanager = 0
                        drawingcontrol = 0
                        healthmanager = healthman(tick, health, hearts)
        drawing(win, restartbutton, 360 - restartbutton.get_width() // 2, 400)
        drawing(win, quitbutton, 360 - quitbutton.get_width() // 2, 600)
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
