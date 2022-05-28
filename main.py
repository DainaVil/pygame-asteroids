import pygame as pg
from pygame.locals import *
from sys import exit
from spaceship import *
from asteroid import *
from explosion import *
from settings import *
from utils import draw_area, draw_text, get_random_coords

class Game:
    
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Asteroids')

        self.game_stopped = True
        self.lives = LIVES
        self.points = 0

        self.bg = pg.image.load('graphic/space.jpeg').convert()
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.screen.blit(self.bg, (0,0))
        self.clock = pg.time.Clock()
        self.timer = 0

        draw_text(self.screen, f'LIVES: {self.lives}', FONT, pg.Color('WHITE'), 10, 10)
        draw_text(self.screen, f'POINTS: {self.points}', FONT, pg.Color('WHITE'), 10, 40)
        
        # добавляем объекты
        self.spaceship = Spaceship()
        self.rockets = pg.sprite.Group()
        self.asteroids = pg.sprite.Group()
        self.bg_asteroids = pg.sprite.Group()
        self.explosions = pg.sprite.Group()

        for _ in range(DEF_ASTEROID_AMOUNT):
            while True: 
                coords = get_random_coords()
                if coords.distance_to(self.spaceship.coords) > MIN_DISTANCE:
                    break
            self.asteroids.add(Asteroid(coords))

        for i in range(DEF_ASTEROID_AMOUNT * 2):
            coords = get_random_coords()
            self.bg_asteroids.add(Asteroid(coords, transperent=True))

    def mainloop(self):
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    exit()
                if event.type == KEYDOWN:
                    keys = pg.key.get_pressed()
                    if keys[pg.K_ESCAPE]:
                        self.game_stopped = True
                    elif keys[K_SPACE] and not self.game_stopped:
                        self.rockets.add(self.spaceship.shoot())
                if event.type == MOUSEBUTTONDOWN and self.game_stopped:
                    pos = pg.mouse.get_pos()
                    if (200 < pos[0] < 800) and (200 < pos[1] < 500):
                        self.game_stopped = False


            if not self.game_stopped:
                keys = pg.key.get_pressed()            
                if keys[K_RIGHT]:
                    self.spaceship.rotate(clockwise=True)
                elif keys[K_LEFT]:
                    self.spaceship.rotate(clockwise=False)
                if keys[K_UP]:
                    self.spaceship.accelerate()
                if not keys[K_UP]:
                    self.spaceship.stopped=True

                # пускать лазерные лучи :)
                # if keys[K_SPACE]:
                #     self.rockets.add(self.spaceship.shoot())

                self.spaceship.move(stop=True)

                for a in self.asteroids:
                    if a.collides_with(self.spaceship):
                        a.kill()
                        self.explosions.add(Explosion(a.coords))
                        # self.add_asteroid(self.asteroids)
                        self.spaceship.kill()
                        # self.explosions.add(Explosion(self.spaceship.coords))
                        self.spaceship = Spaceship()
                        if self.lives == 0:
                            self.lives = 0
                            self.points = 0
                            self.game_stopped = True
                        self.lives -= 1
                    for r in self.rockets:
                        if a.collides_with(r):
                            a.kill()
                            self.explosions.add(Explosion(a.coords))
                            r.kill()
                            # self.add_asteroid(self.asteroids)
                            self.points += 1

            else:
                self.lives = 3
                self.points = 0
            
            if self.timer == FREQUENCY:
                self.add_asteroid(self.asteroids)
                self.timer = 0
            else: 
                self.timer += 1                    
            self.draw()
            self.clock.tick(FPS)
            

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        
        if not self.game_stopped:
            self.explosions.clear(self.screen, self.bg)
            self.explosions.draw(self.screen)
            self.asteroids.clear(self.screen, self.bg)
            self.asteroids.draw(self.screen)
            self.rockets.clear(self.screen, self.bg)
            self.rockets.draw(self.screen)

            for e in self.explosions:
                e.update()
            for a in self.asteroids:
                a.update()
            for r in self.rockets:
                r.update()
            self.spaceship.update(self.screen)
        else:
            for ba in self.bg_asteroids:
                ba.update()
            
            self.bg_asteroids.clear(self.screen, self.bg)
            self.bg_asteroids.draw(self.screen)

            draw_area(self.screen, pg.Color('white'))
            draw_text(self.screen, f'ASTEROIDS', BIG_FONT, (30, 30, 80), 225, 250)
            draw_text(self.screen, f'Click here to start', FONT, (30, 30, 80), 360, 400)
            
        
        draw_text(self.screen, f'LIVES: {self.lives}', FONT, pg.Color('WHITE'), 10, 10)
        draw_text(self.screen, f'POINTS: {self.points}', FONT, pg.Color('WHITE'), 10, 40)
        pg.display.update()

    def add_asteroid(self, asteroids):
        if len(asteroids) < MAX_ASTEROID_AMOUNT:
            while True: 
                coords = get_random_coords()
                if coords.distance_to(self.spaceship.coords) > MIN_DISTANCE:
                    break
            asteroids.add(Asteroid(coords))

if __name__ == '__main__':
    game = Game()
    game.mainloop()
