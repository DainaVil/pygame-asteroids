import pygame as pg
from settings import *

class Rocket(pg.sprite.Sprite):

    def __init__(self, coodrs, velocity, direction) -> None:
        super().__init__()

        self.max_x = WIDTH
        self.max_y = HEIGHT
        self.velocity = pg.Vector2(velocity)
        self.coords = pg.Vector2(coodrs)
        self.direction = pg.Vector2(direction)
        self.lifetime = LIFETIME

        # прорисовка ракеты
        self.image = pg.image.load('graphic/rocket1.png').convert_alpha()
        self.image = pg.transform.scale(self.image, ROCKET_SIZE)
        angle = self.direction.angle_to(UP)
        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.coords)
        self.radius = self.image.get_width() / 2
        
    def update(self):
            if self.lifetime > 0:
                self.lifetime -= 1
            else:
                self.kill()

            self.move()
            self.rect = self.image.get_rect(center=self.coords)
            self.transition()

    def move(self):
        self.coords += self.velocity

    # уничтожение при выходе за границы экрана
    def transition(self):
        if (self.coords[0] + self.radius < 0) or \
            (self.coords[0] - self.radius > self.max_x) or \
            (self.coords[1] + self.radius < 0) or \
            (self.coords[1] - self.radius > self.max_y):
            
            self.kill()
