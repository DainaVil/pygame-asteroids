from pygame import Vector2
import pygame as pg
from random import randrange
from settings import HEIGHT, MENU_COODRS, MENU_SIZE, WIDTH

# возвращает случайные координаты в пределах экрана
def get_random_coords():
    return Vector2(randrange(WIDTH), randrange(HEIGHT))

# прорисовка текста
def draw_text(screen, text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# прорисовка заставки
def draw_area(screen, color):
    img = pg.Surface(MENU_SIZE)
    img.fill(color)
    img.set_alpha(100)
    rect = img.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(img, MENU_COODRS)