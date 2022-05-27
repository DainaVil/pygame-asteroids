from random import uniform
import pygame as pg
from settings import *

class Asteroid(pg.sprite.Sprite):

    def __init__(self, position, transperent=False) -> None:
        super().__init__()

        self.max_x = WIDTH
        self.max_y = HEIGHT
        self.transperent = transperent

        # координаты и скорость представляют собой векторы
        self.coords = pg.Vector2(position)
        self.velocity = pg.Vector2(uniform(-1, 1) * ASTEROID_SPEED, uniform(-1, 1) * ASTEROID_SPEED)
        
        # прорисовка астероида
        self.image = pg.image.load('graphic/asteroid.png').convert_alpha()
        self.dir = pg.Vector2(uniform(-1, 1), uniform(-1, 1))
        angle = self.dir.angle_to(UP)
        self.image = pg.transform.rotate(self.image, angle)
        self.image = pg.transform.scale(self.image, (ASTEROID_SIZE, ASTEROID_SIZE))
        
        self.rect = self.image.get_rect(center=self.coords)
        if self.transperent:
            self.image.set_alpha(170)
            self.velocity = pg.math.Vector2(1, 0) * ASTEROID_SPEED
        self.image.blit(self.image, self.rect)
        self.radius = self.image.get_width() / 2
        
    def update(self):
        self.coords += self.velocity
        self.rect = self.image.get_rect(center=self.coords)
        self.transition()

    # смена координат при выходе за границы экрана
    def transition(self):
        if self.coords[0] + ASTEROID_SIZE/2 < 0:
            self.coords[0] += self.max_x + ASTEROID_SIZE
        elif self.coords[0] - ASTEROID_SIZE/2 > self.max_x:
            self.coords[0] -= self.max_x + ASTEROID_SIZE

        if self.coords[1] + ASTEROID_SIZE/2 < 0:
            self.coords[1] += self.max_y + ASTEROID_SIZE
        elif self.coords[1] - ASTEROID_SIZE/2 > self.max_y:
            self.coords[1] -= self.max_y + ASTEROID_SIZE

    # проверка на столкновение с другим объектом
    def collides_with(self, other_obj):
        distance = self.coords.distance_to(other_obj.coords)
        return distance < self.radius + other_obj.radius - 30