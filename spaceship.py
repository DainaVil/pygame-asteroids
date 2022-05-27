import pygame as pg
from rocket import *
from settings import *

class Spaceship(pg.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()

        self.max_x = WIDTH
        self.max_y = HEIGHT
        self.acceleration = ACCELERATION

        self.coords = pg.Vector2(self.max_x/2, self.max_y/2)
        self.direction = pg.Vector2(UP)
        self.velocity = pg.math.Vector2(UP)
        self.stopped = True
        
        # прорисовка корабля
        self.images = []
        for i in range(1, 3):
            img = pg.image.load(f'graphic/spaceship{i}.png').convert_alpha()
            img = pg.transform.scale(img, (SPACESHIP_SIZE, SPACESHIP_SIZE))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=self.coords)
        self.image.blit(self.image, self.rect)
        self.radius = self.images[0].get_width() / 2
        
    def update(self, surface):
            self.draw(surface)
            self.transition()

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = MOBILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        self.image = self.images[0] if self.stopped else self.images[1]
        # self.image.blit(self.image, self.rect)
        angle = self.direction.angle_to(UP)
        rotated_surface = pg.transform.rotozoom(self.image, angle, 1.0)
        rotated_surface_size = pg.Vector2(rotated_surface.get_size())
        blit_position = self.coords - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
        self.transition()

    def move(self, stop = False):
        if stop and self.velocity.as_polar()[0] > 0:
            self.velocity *= RESISTANCE
        self.coords += self.velocity
        
    # ускорение    
    def accelerate(self):
        self.velocity += self.direction * self.acceleration 
        # проверка на достижение максимальной скорости
        if self.velocity.magnitude() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)
        self.stopped=False
        # self.move()

    # пуск ракеты
    def shoot(self):
        rocket_velocity = self.direction * ROCKET_SPEED + self.velocity
        rocket =  Rocket(self.coords, rocket_velocity, self.direction)
        return rocket

    # смена координат при выходе за границы экрана
    def transition(self):
        if self.coords[0] + self.radius < 0:
            self.coords[0] += self.max_x + self.radius*2
        elif self.coords[0] - self.radius > self.max_x:
            self.coords[0] -= self.max_x + self.radius*2

        if self.coords[1] + self.radius < 0:
            self.coords[1] += self.max_y + self.radius*2
        elif self.coords[1] - self.radius > self.max_y:
            self.coords[1] -= self.max_y + self.radius*2

    def collides_with(self, other_obj):
        distance = self.coords.distance_to(other_obj.coords)
        return distance < self.radius + other_obj.radius
