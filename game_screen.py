import pygame as pg
from config import *
from random import choice


class GameScreen:
    background_images_list = None
    spaceship_image = None

    @staticmethod
    def init_stat():
        GameScreen.background_images_list = [
            pg.image.load('assets/space/space1.png').convert_alpha(),
            pg.image.load('assets/space/space2.png').convert_alpha(),
            pg.image.load('assets/space/space3.png').convert_alpha()
        ]

        GameScreen.spaceship_image = pg.image.load('assets/spaceship_image.png').convert_alpha()

    class Background:
        def __init__(self, y):
            self.image = choice(GameScreen.background_images_list)
            self.y = y
            self.speed = 0.5

        def move(self):
            self.y += self.speed
            if self.y > HEIGHT14:
                self.y -= HEIGHT14 * BG_COUNT
                self.image = choice(GameScreen.background_images_list)

    def __init__(self):
        GameScreen.init_stat()

        self.game_sur = pg.Surface((MAIN_WIDTH, HEIGHT14))
        self.backgrounds = [GameScreen.Background(-1 * HEIGHT14 * i) for i in range(BG_COUNT)]

    def update(self):
        self.game_sur.fill((0, 0, 0))
        for background in self.backgrounds:
            self.game_sur.blit(background.image, (0, background.y))
            background.move()

        self.game_sur.blit(GameScreen.spaceship_image, (500, 500))
