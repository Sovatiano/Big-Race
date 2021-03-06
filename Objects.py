import random
import pygame

class spawning(pygame.sprite.Sprite):
    def __init__(self, objects, speed, tick, spis, *group):
        super().__init__(*group)
        self.spis = spis
        self.ints = [1, 4, 7]
        self.x = random.choice(self.ints)
        self.objects = objects
        self.image = random.choice(self.objects)
        self.spis.append(self.objects.index(self.image))
        self.speed = speed
        self.tick = tick
        self.rect = self.image.get_rect()
        self.rect.x = 80 * self.x + 5
        self.rect.y = -500
        self.mask = pygame.mask.from_surface(self.image)
        self.random = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed * self.tick * self.random / 1000

class drawtire(pygame.sprite.Sprite):
    def __init__(self, tiremark, x, y, speed, tick, *group):
        super().__init__(*group)
        self.speed = speed
        self.tick = tick
        self.image = tiremark
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        self.rect.y += self.speed * self.tick / 1000