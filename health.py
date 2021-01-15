import pygame


class hearts(pygame.sprite.Sprite):
    def __init__(self, heart, x, y, speed, tick, *group):
        super().__init__(*group)
        self.speed = speed
        self.tick = tick
        self.image = heart
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.movingup = True
        self.movingdown = False

    def update(self):
        if self.rect.y < 40:
            self.movingup = False
            self.movingdown = True
        if self.rect.y > 60:
            self.movingup = True
            self.movingdown = False
        if self.movingup:
            self.rect.y -= self.speed * self.tick / 3000
        if self.movingdown:
            self.rect.y += self.speed * self.tick / 3000