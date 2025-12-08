import pygame as pg
from config import *
from random import choice
from utils import ImgLdr
from player import Player, InertialMotion


class GameScreen:
    class Background:
        def __init__(self, y):
            self.background_images_list = [
                ImgLdr.dict["BG_space1"],
                ImgLdr.dict["BG_space2"],
                ImgLdr.dict["BG_space3"]
            ]
            self.image = choice(self.background_images_list)
            self.y = y
            self.speed = 0.5

        def move(self):
            self.y += self.speed
            if self.y > HEIGHT14:
                self.y -= HEIGHT14 * BG_COUNT
                self.image = choice(self.background_images_list)

    def __init__(self):
        self.game_sur = pg.Surface((MAIN_WIDTH, HEIGHT14))
        self.backgrounds = [GameScreen.Background(-1 * HEIGHT14 * i) for i in range(BG_COUNT)]

        self.player = Player()
        self.x_inertial_motion = InertialMotion(100)
        self.y_inertial_motion = InertialMotion(100)

    def update(self):
        self.game_sur.fill((0, 0, 0))
        for background in self.backgrounds:
            self.game_sur.blit(background.image, (0, background.y))
            background.move()

        self.check_pressed()
        self.player.update()
        self.check_player_position()
        self.game_sur.blit(self.player.cur_sprite, (self.player.x, self.player.y))

    def process_keyboard(self, key) -> None:
        pass

    def check_pressed(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and not keys[pg.K_s]:
            self.player.y_speed = self.y_inertial_motion.update_speed(self.player.y_speed, -1 * ACCELERATION)
        if keys[pg.K_s] and not keys[pg.K_w]:
            self.player.y_speed = self.y_inertial_motion.update_speed(self.player.y_speed, ACCELERATION)
        if keys[pg.K_a] and not keys[pg.K_d]:
            self.player.x_speed = self.x_inertial_motion.update_speed(self.player.x_speed, -1 * ACCELERATION)
        if keys[pg.K_d] and not keys[pg.K_a]:
            self.player.x_speed = self.x_inertial_motion.update_speed(self.player.x_speed, ACCELERATION)

    def check_player_position(self):
        if self.player.y < 0:
            self.player.y = 0
            self.player.y_speed *= -0.5
        elif self.player.y + self.player.size[1] > HEIGHT14:
            self.player.y = HEIGHT14 - self.player.size[1]
            self.player.y_speed *= -0.5

        if self.player.x < 0:
            self.player.x = 0
            self.player.x_speed *= -0.5
        elif self.player.x + self.player.size[0] > MAIN_WIDTH:
            self.player.x = MAIN_WIDTH - self.player.size[0]
            self.player.x_speed *= -0.5
