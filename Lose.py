import pygame


class lose(pygame.sprite.Sprite):
    def __init__(self, carmask, objectmask, *group):
        super().__init__(*group)
        self.carmask = carmask
        self.objectmask = objectmask

    def update(self):
        print(1)
        if pygame.sprite.collide_mask(self.carmask, self.objectmask):
            print('ololol')
