import pygame as pg
from utils import ImgLdr
from sprite_animation import SpriteAnimation
from config import *


class Player:
    def __init__(self):
        self.cur_sprite: pg.Surface = ImgLdr.dict["spaceship_move3"]
        self.animations = {
            "move": SpriteAnimation([ImgLdr.dict[f"spaceship_move{i}"] for i in range(4)],
                                    120,
                                    cyclic=True),
            "braking": SpriteAnimation([ImgLdr.dict[f"spaceship_braking{i}"] for i in range(4)],
                                       120,
                                       cyclic=True)
        }
        self.cur_anim: str = "move"
        self.x = 500
        self.y = 500
        self.size = self.cur_sprite.get_rect().size

        # Характеристики
        self.x_speed = 0
        self.y_speed = 0
        self.health = 3
        self.speed = 1

    def update(self):
        # print(self.cur_anim)
        self.animations[self.cur_anim].update()
        self.cur_sprite = self.animations[self.cur_anim].get_current_frame()

        self.x += self.x_speed
        self.y += self.y_speed


class InertialMotion:
    def __init__(self, delay_ms):
        self.delay = delay_ms
        self.last_update = pg.time.get_ticks()

    def update_speed(self, speed, growth, braking=False):
        current_time = pg.time.get_ticks()
        if current_time - self.last_update > self.delay:
            self.last_update = current_time

            # Положительный и отрицательный разгон
            if not braking:
                new_speed = speed + growth
                if new_speed < -1 * MAX_PLAYER_SPEED:
                    speed = -1 * MAX_PLAYER_SPEED
                elif new_speed > MAX_PLAYER_SPEED:
                    speed = MAX_PLAYER_SPEED
                else:
                    speed = new_speed
            # Торможение
            else:
                speed -= self.copysign(min(abs(speed), abs(growth)), speed)

        return speed

    def copysign(self, x, y):
        if y > 0:
            return abs(x)
        elif y < 0:
            return -1 * abs(x)
        else:
            return 0
