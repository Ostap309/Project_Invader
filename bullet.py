import pygame as pg
from config import *


class Bullet:
    def __init__(self, sprite: pg.Surface, x: int, y: int, speed: float, vector: int, enemy=False):
        self.sprite = sprite
        self.enemy = enemy

        self.speed = speed
        self.vector = vector

        self.x = x
        self.y = y

    def move(self) -> bool:
        self.y += self.speed * self.vector
        if self.y < -10:
            return True

        return False
