import pygame as pg
import copy

from bullet import Bullet
from config import *
from random import choice
from utils import ImgLdr
from player import Player, InertialMotion


class GameScreen:
    class Background:
        def __init__(self, y: int) -> None:
            self.background_images_list = [
                ImgLdr.dict["BG_space1"],
                ImgLdr.dict["BG_space2"],
                ImgLdr.dict["BG_space3"]
            ]
            self.image = choice(self.background_images_list)
            self.y = y
            self.speed = BG_SPEED

        # Метод цикличного сдвига вниз объекта фона
        def move(self) -> None:
            self.y += self.speed
            if self.y > HEIGHT14:
                self.y -= HEIGHT14 * BG_COUNT
                self.image = choice(self.background_images_list)

    def __init__(self) -> None:
        self.game_sur = pg.Surface((MAIN_WIDTH, HEIGHT14))
        self.backgrounds = [GameScreen.Background(-1 * HEIGHT14 * i) for i in range(BG_COUNT)]

        # Создание игрока
        self.player = Player()

        # Создание классов движения с инерцией по осям X и Y
        self.x_inertial_motion = InertialMotion(100)
        self.y_inertial_motion = InertialMotion(100)

        # Список снарядов на экране
        self.bullet_list = []

    def update(self) -> None:
        # Создание динамического фона
        self.game_sur.fill((0, 0, 0))
        for background in self.backgrounds:
            self.game_sur.blit(background.image, (0, background.y))
            background.move()

        # Обновление отображения игрока
        self.player.update()
        self.check_player_position()
        self.game_sur.blit(self.player.cur_sprite, (self.player.x, self.player.y))
        self.game_sur.blit(self.player.slot1.cur_sprite,
                           (self.player.x + self.player.size[0] / 2 - 10, self.player.y - 2))

        # Отображение снарядов
        # print(len(self.bullet_list))

        for bullet in copy.copy(self.bullet_list):
            self.game_sur.blit(bullet.sprite, (bullet.x, bullet.y))
            if bullet.move():
                self.bullet_list.remove(bullet)

    # Обработка нажатий клавиш
    def check_clicks(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN and event.key == pg.K_x:
            self.player.cur_anim = "braking"
        elif event.type == pg.KEYUP and event.key == pg.K_x:
            self.player.cur_anim = "move"

    # Обработка удержания клавиш
    def check_pressed(self, keys: pg.key.ScancodeWrapper) -> None:
        if keys[pg.K_x]:
            self.player.y_speed = self.y_inertial_motion.update_speed(self.player.y_speed, ACCELERATION, braking=True)
            self.player.x_speed = self.x_inertial_motion.update_speed(self.player.x_speed, ACCELERATION, braking=True)
            return

        if keys[pg.K_w] and not keys[pg.K_s]:
            self.player.y_speed = self.y_inertial_motion.update_speed(self.player.y_speed, -1 * ACCELERATION)
        if keys[pg.K_s] and not keys[pg.K_w]:
            self.player.y_speed = self.y_inertial_motion.update_speed(self.player.y_speed, ACCELERATION)
        if keys[pg.K_a] and not keys[pg.K_d]:
            self.player.x_speed = self.x_inertial_motion.update_speed(self.player.x_speed, -1 * ACCELERATION)
        if keys[pg.K_d] and not keys[pg.K_a]:
            self.player.x_speed = self.x_inertial_motion.update_speed(self.player.x_speed, ACCELERATION)

        # Вооружение
        if pg.mouse.get_pressed()[0]:
            is_shoot = self.player.slot1.fire()

            if is_shoot:
                self.bullet_list.append(Bullet(
                    ImgLdr.dict["bullet"],
                    self.player.x + self.player.size[0] / 2 - 5,
                    self.player.y,
                    5.5,
                    -1))

    def check_player_position(self) -> None:
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
