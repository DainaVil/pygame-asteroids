import pygame as pg
from settings import *

class Explosion(pg.sprite.Sprite):
    def __init__(self, coords) -> None:
        super().__init__()

        self.coords = coords
        # прорисовка взрыва
        self.images = []
        for i in range(1, 6):
            img = pg.image.load(f'graphic/explosion{i}.png').convert_alpha()
            img = pg.transform.scale(img, EXPLOSION_SIZE)
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=self.coords)
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter >= EXPLOSION_SPEED and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # уничтожение при завершении анимации
        if self.index >= len(self.images) - 1 and self.counter >= EXPLOSION_SPEED:
            self.kill()

