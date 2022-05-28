import pygame as pg

pg.init()

# Шрифты
FONT = pg.font.SysFont('beermoney', 40)
BIG_FONT = pg.font.SysFont('beermoney', 140)

# Общие настройки
WIDTH = 1000
HEIGHT = 800
FPS = 60
UP = pg.Vector2(0, -1)
LIVES = 3
MENU_SIZE = pg.Vector2(600, 300)
MENU_COODRS = pg.Vector2(200, 200)

# Настройки астероидов
DEF_ASTEROID_AMOUNT = 5
MAX_ASTEROID_AMOUNT = 10
ASTEROID_SPEED = 1
ASTEROID_SIZE = 130
MIN_DISTANCE = 200 # минимальное расстояние до ракеты при генерации астероида
FREQUENCY = 70 # частота появления на экране

# Настройки корабля
MOBILITY = 5 # отвечает за скорость поворота
MAX_SPEED = 5
SPACESHIP_SIZE = 100
ACCELERATION = 2 # ускорение
RESISTANCE = .97 # сопротивление среды

# Rocket settings
ROCKET_SPEED = 10
ROCKET_SIZE = (10, 30)
LIFETIME = 50

# Explosion settings
EXPLOSION_SIZE = (150, 150)
EXPLOSION_SPEED = 5